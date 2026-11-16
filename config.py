import logging
from os import getenv
from telethon import TelegramClient
from AltBots.data import ALTRON

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

API_ID = int(getenv("API_ID", "10079905"))
API_HASH = getenv("API_HASH", "e4a5fa251e2e055f26e5c2add8401530")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Sirf 2 tokens — baaki sab gone
BOT_TOKEN  = getenv("BOT_TOKEN",  "8605571186:AAFj3tljBt2scB77su4VMCpHP1Nf4Ic2htE")
BOT_TOKEN2 = getenv("BOT_TOKEN2", "8994968874:AAFHej-HNZcSPHivgeg9wE9wuX_4ZtiT9b0")

BOT_TOKENS = [t for t in [BOT_TOKEN, BOT_TOKEN2] if t and t.strip()]

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8841848847").split()))
for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8841848847"))
if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

ACTIVE_BOT_COUNT = int(getenv("ACTIVE_BOT_COUNT", "2"))
START_ALL = getenv("START_ALL", "true").lower() in ("1", "true", "yes")

clients = {}

# Sirf X1 aur X2 — X3..X10 nahi
X1 = TelegramClient("X1", API_ID, API_HASH)
X2 = TelegramClient("X2", API_ID, API_HASH)