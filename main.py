import sys
import glob
import asyncio
import logging
import importlib
import importlib.util
import urllib3
from pathlib import Path
from telethon.errors.rpcerrorlist import FloodWaitError

from config import (
    X1, X2,
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
            load_plugins(plugin_name)

    print("\nAltron has successfully imported all modules.")

    async def main():
        try:
            from AltBots.db import init_db, load_sudoers
            if await init_db():
                loaded = await load_sudoers(OWNER_ID)
                for uid in loaded:
                    if uid not in SUDO_USERS:
                        SUDO_USERS.append(uid)
                print(f"✅ Sudo loaded from DB: {len(SUDO_USERS)} users")
            else:
                print("⚠️ DB offline — sudo memory/env only")
        except Exception as e:
            print(f"⚠️ DB init skip: {e}")

        all_bots   = [X1, X2]
        all_tokens = BOT_TOKENS[:2]   # hard cap at 2

        if not all_tokens:
            print("❌ Koi BOT_TOKEN env mein nahi mila.")
            return

        started_clients = []
        for idx, (client, token) in enumerate(zip(all_bots, all_tokens), start=1):
            result = await start_client(client, f"X{idx}", token)
            if result is not None:
                clients[f"X{idx}"] = result
                started_clients.append(result)

        if not started_clients:
            print("❌ Koi bot start nahi hua.")
            return

        print(f"✅ {len(started_clients)} bot(s) started successfully.")

        tasks = [asyncio.create_task(c.run_until_disconnected()) for c in started_clients]
        await asyncio.gather(*tasks)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()