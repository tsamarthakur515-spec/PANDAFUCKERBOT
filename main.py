import sys
import glob
import asyncio
import logging
import importlib
import urllib3
import os
from pathlib import Path
from telethon.errors.rpcerrorlist import FloodWaitError

from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    BOT_TOKENS, ACTIVE_BOT_COUNT, START_ALL,
    clients, SUDO_USERS, OWNER_ID,
)

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def load_plugins(plugin_name):
    path = Path(f"AltBots/modules/{plugin_name}.py")
    spec = importlib.util.spec_from_file_location(f"AltBots.modules.{plugin_name}", path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["AltBots.modules." + plugin_name] = load
    print("Altron has Imported " + plugin_name)


async def start_client(client, name, token):
    """Start a single TelegramClient in the running async context."""
    if not token:
        logging.info("No token for %s, skipping", name)
        return None
    try:
        await client.start(bot_token=token)
        logging.info("%s started successfully", name)
        return client
    except FloodWaitError as e:
        wait_seconds = getattr(e, "seconds", None) or 0
        logging.warning("FloodWaitError on %s: waiting %s seconds", name, wait_seconds)
        if wait_seconds > 0:
            await asyncio.sleep(wait_seconds + 1)
            try:
                await client.start(bot_token=token)
                logging.info("%s started after wait", name)
                return client
            except Exception as e2:
                logging.error("Failed to start %s after wait: %s", name, e2)
                return None
        return None
    except Exception as exc:
        logging.error("Error starting %s: %s", name, exc)
        return None


if __name__ == "__main__":
    print("Loading modules...")
    files = glob.glob("AltBots/modules/*.py")
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    print("\nAltron has successfully imported all modules.")

    async def main():
        # DB + persistent sudo
        try:
            from AltBots.db import init_db, load_sudoers

            if await init_db():
                loaded = await load_sudoers(OWNER_ID)
                # merge into live SUDO_USERS list (keep env + ALTRON too)
                for uid in loaded:
                    if uid not in SUDO_USERS:
                        SUDO_USERS.append(uid)
                print(f"✅ Sudo loaded from DB: {len(SUDO_USERS)} users")
            else:
                print("⚠️ DB offline — sudo memory/env only")
        except Exception as e:
            print(f"⚠️ DB init skip: {e}")

        all_tokens = BOT_TOKENS
        to_start = all_tokens if START_ALL else all_tokens[:ACTIVE_BOT_COUNT]

        bot_clients = []
        all_bots = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

        for idx, token in enumerate(to_start, start=1):
            if idx > len(all_bots):
                break
            client = all_bots[idx - 1]
            if client is None:
                logging.info("Client X%s not available, skipping", idx)
                continue
            bot_clients.append((client, f"X{idx}", token))

        started_clients = []
        for client, name, token in bot_clients:
            result = await start_client(client, name, token)
            if result is not None:
                clients[name] = result
                started_clients.append(result)

        if not started_clients:
            logging.error("No clients started. Exiting.")
            return

        tasks = []
        for c in started_clients:
            tasks.append(asyncio.create_task(c.run_until_disconnected()))
            logging.info("Scheduled %s for updates", next(
                (k for k, v in clients.items() if v is c), "?"
            ))

        await asyncio.gather(*tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
