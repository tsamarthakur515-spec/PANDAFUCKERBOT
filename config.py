
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

CMD_HNDLR = getenv("CMD_HNDLR", ".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# ONLY 2 BOT TOKENS
BOT_TOKEN = getenv(
    "BOT_TOKEN",
    "9282475067:AAFvwbmOFcPWpB9c7vpf6VOwvPbLz3Gb6MM"
)

BOT_TOKEN2 = getenv(
    "BOT_TOKEN2",
    "9244859863:AAE_z1k1IFfPwg-REepG7dy12B9XbTWKx0E"
)

BOT_TOKENS = [
    token for token in (BOT_TOKEN, BOT_TOKEN2)
    if token and token.strip()
]

# SUDO USERS
SUDO_USERS = list(
    map(int, getenv("SUDO_USERS", "8841848847").split())
)

for user in ALTRON:
    if user not in SUDO_USERS:
        SUDO_USERS.append(user)

OWNER_ID = int(getenv("OWNER_ID", "8841848847"))

if OWNER_ID not in SUDO_USERS:
    SUDO_USERS.append(OWNER_ID)

# MAXIMUM 2 ACTIVE BOTS
ACTIVE_BOT_COUNT = min(
    2, max(0, int(getenv("ACTIVE_BOT_COUNT", "2")))
)

START_ALL = getenv("START_ALL", "true").lower() in (
    "1", "true", "yes"
)

clients = {}

# ONLY X1 AND X2
X1 = TelegramClient("X1", API_ID, API_HASH)
X2 = TelegramClient("X2", API_ID, API_HASH)
