import sys
import glob
import asyncio
import logging
import importlib
import urllib3
import os
from flask import Flask
from threading import Thread
from pathlib import Path
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, clients

# --- KEEP ALIVE SECTION START ---
app_web = Flask(__name__)

@app_web.route('/')
@app_web.route('/health') # Snapdeploy health check ke liye
def home():
    return "Altron Bot is Running!", 200

def run_web():
    # Snapdeploy/Render ke port ko auto-detect karega
    port = int(os.environ.get("PORT", 8000))
    try:
        app_web.run(host='0.0.0.0', port=port)
    except OSError as e:
        logging.warning("Web server failed to start on port %s: %s", port, e)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()
# --- KEEP ALIVE SECTION END ---

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

# Plugins load karne se pehle web server start karein
if __name__ == "__main__":
    keep_alive()
    print("Web Server Started for Health Check...")

    files = glob.glob("AltBots/modules/*.py")
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    print("\nAltron has successfully imported all modules.\nMy Master ---> @Theshonaqueen")

    async def main():
        # Sabhi clients ko start/connect karein aur sirf connected clients ko run_until_disconnected pe daalein
        tasks = []

        # Prefer clients that were started/registered in config (clients dict).
        for name, c in clients.items():
            if c is None:
                logging.info("Configured client %s is None, skipping", name)
                continue
            try:
                # Ensure client is connected; connect() is a coroutine
                if hasattr(c, "is_connected") and c.is_connected():
                    tasks.append(c.run_until_disconnected())
                else:
                    await c.connect()
                    if hasattr(c, "is_connected") and c.is_connected():
                        tasks.append(c.run_until_disconnected())
                    else:
                        logging.warning("Client %s failed to connect", name)
            except Exception as e:
                logging.warning("Configured client %s couldn't connect/run: %s", name, e)

        # Fallback: try to connect any X1..X10 client objects if clients dict was empty or some are missing
        if not tasks:
            for client in (X1, X2, X3, X4, X5, X6, X7, X8, X9, X10):
                if client is None:
                    continue
                try:
                    if hasattr(client, "is_connected") and client.is_connected():
                        tasks.append(client.run_until_disconnected())
                        continue
                    await client.connect()
                    if hasattr(client, "is_connected") and client.is_connected():
                        tasks.append(client.run_until_disconnected())
                    else:
                        logging.warning("Client %s failed to connect", getattr(client, 'session', repr(client)))
                except Exception as e:
                    logging.warning("Client %s skipped: %s", getattr(client, 'session', repr(client)), e)

        if not tasks:
            logging.error("No clients available to run. Exiting.")
            return

        await asyncio.gather(*tasks)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
