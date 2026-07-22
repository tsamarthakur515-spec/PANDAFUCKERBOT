
import logging
import time
from os import getenv
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError
from AltBots.data import ALTRON

# Logging setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Telegram API details
API_ID = int(getenv("API_ID", "18136872"))
API_HASH = getenv("API_HASH", "312d861b78efcd1b02183b2ab52a83a4")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "rand")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Bot tokens should come from environment variables; fallback to empty strings if not set.
BOT_TOKEN = "8236003776:AAEBvVgpiCQRvMNqnZz765VbC0qf4i8afaY"
BOT_TOKEN2 = "8509012033:AAG4ELcUnwtH90KbBeJQSqkeu3xhIiTYB_k"
BOT_TOKEN3 = "8907901853:AAFSuKLHO5TQ5bXo0ntpJBFTAlz4zbOl8Gg"
BOT_TOKEN4 = "8711056379:AAFYZgj_LWfg04yHLU-L1eY4TnSATNp0zRs"
BOT_TOKEN5 = "8862433888:AAHVlAVTKLcJvm8wdrKdfMysSS3OBs5ccLw"
BOT_TOKEN6 = "8766121545:AAFE6uv4nr84WBeERexxq5bEf75e2SlTyrc"
BOT_TOKEN7 = "8596765113:AAGZLdNgNDJPWMOElYosF-gi5Xxaew51ps4"
BOT_TOKEN8 = "8319792839:AAHJMZADSr3fxQR8879vD_8asQJfIOl9qzA"
BOT_TOKEN9 = "8144493217:AAEs6-TvErgNKiI7Tp2d2iuhqXyu4Casigk"
BOT_TOKEN10 = "8415072105:AAEVzmQ-5axyxv62l3TXngRAPPG10p2lr-Y"

# Owner and Sudo users
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7311297618").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8566803656"))
SUDO_USERS.append(OWNER_ID)

# How many bots to start by default. Keep this low to avoid hitting rate limits.
ACTIVE_BOT_COUNT = int(getenv("ACTIVE_BOT_COUNT", "1"))

# Optionally set START_ALL=true to attempt to start all tokens (dangerous for rate limits)
START_ALL = getenv("START_ALL", "false").lower() in ("1", "true", "yes")

# Container for started client objects
clients = {}
# Initialize only the requested number of active bot clients, sequentially and with FloodWait handling.
to_start = BOT_TOKENS if START_ALL else BOT_TOKENS[:ACTIVE_BOT_COUNT]

for idx, token in enumerate(to_start, start=1):
    name = f"X{idx}"
    if not token:
        logging.info("No token provided for %s, skipping", name)
        globals()[name] = None
        continue

    client = TelegramClient(name, API_ID, API_HASH)
    try:
        # start() can raise FloodWaitError; wrap in try/except
        started = client.start(bot_token=token)
        globals()[name] = started
        clients[name] = started
        logging.info("%s started successfully", name)
    except FloodWaitError as e:
        wait_seconds = getattr(e, "seconds", None) or 0
        logging.warning("FloodWaitError when starting %s: waiting %s seconds", name, wait_seconds)
        if wait_seconds > 0:
            time.sleep(wait_seconds + 1)
            # retry once after waiting
            try:
                started = client.start(bot_token=token)
                globals()[name] = started
                clients[name] = started
                logging.info("%s started successfully after waiting", name)
            except Exception as e2:
                logging.error("Failed to start %s after wait: %s", name, e2)
                globals()[name] = None
        else:
            globals()[name] = None
    except Exception as exc:
        logging.error("Unexpected error while starting %s: %s", name, exc)
        globals()[name] = None

# Fill remaining X2..X10 names with None if they were not created
for i in range(1, 11):
    varname = f"X{i}"
    if varname not in globals():
        globals()[varname] = None

