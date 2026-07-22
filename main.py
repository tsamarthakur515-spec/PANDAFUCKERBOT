import sys
import glob
import asyncio
import logging
import importlib
import urllib3
import os
from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, clients

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


if __name__ == "__main__":
    # Load all modules (no web server / Flask anymore)
    print("Loading modules...")
    files = glob.glob("AltBots/modules/*.py")
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    print("\nAltron has successfully imported all modules.")

    async def main():
        # Schedule run_until_disconnected only for clients that are connected (or can connect now).
        tasks = []

        for name, c in clients.items():
            if c is None:
                logging.info("Configured client %s is None, skipping", name)
                continue
            try:
                # If already connected, schedule running
                if hasattr(c, "is_connected") and c.is_connected():
                    tasks.append(asyncio.create_task(c.run_until_disconnected()))
                    logging.info("Scheduled %s (already connected)", name)
                    continue

                # Otherwise, try to connect (coroutine)
                await c.connect()
                if hasattr(c, "is_connected") and c.is_connected():
                    tasks.append(asyncio.create_task(c.run_until_disconnected()))
                    logging.info("Scheduled %s after connect", name)
                else:
                    logging.warning("Client %s failed to connect", name)
            except Exception as e:
                logging.warning("Configured client %s couldn't connect/run: %s", name, e)

        # Fallback: try raw X1..X10 objects in case clients dict is empty
        if not tasks:
            for idx, client in enumerate((X1, X2, X3, X4, X5, X6, X7, X8, X9, X10), start=1):
                name = f"X{idx}"
                if client is None:
                    continue
                try:
                    if hasattr(client, "is_connected") and client.is_connected():
                        tasks.append(asyncio.create_task(client.run_until_disconnected()))
                        logging.info("Scheduled %s (already connected)", name)
                        continue
                    await client.connect()
                    if hasattr(client, "is_connected") and client.is_connected():
                        tasks.append(asyncio.create_task(client.run_until_disconnected()))
                        logging.info("Scheduled %s after connect", name)
                    else:
                        logging.warning("Client %s failed to connect", name)
                except Exception as e:
                    logging.warning("Client %s skipped: %s", name, e)

        if not tasks:
            logging.error("No clients available to run. Exiting.")
            return

        await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
