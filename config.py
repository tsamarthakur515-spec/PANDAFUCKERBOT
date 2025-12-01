import logging
from telethon import TelegramClient
from os import getenv
from AltBots.data import ALTRON

# Logging setup
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Telegram API details
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "rand")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Bot Tokens (only one active)
BOT_TOKEN = "8515132021:AAEVqzQ9QWdYPi4ZSYNPBVMOAFR7GQMosmE"
BOT_TOKEN2 = "8346635934:AAGPF37frz2DYuZlIkDj5YA5_Eps8N-w3hQ"
BOT_TOKEN3 = "8189431067:AAExcITIzekPIdN1XLMD1UcrLCByp3DK9m8"
BOT_TOKEN4 = "7935654265:AAGN3YRZ3aRSLWTqzVV-9Bvi-k8xSPULtVw"
BOT_TOKEN5 = "7998579547:AAFxdxk90nm3v7Fi43Hb3J9FX9X9Hdw2iZA"
BOT_TOKEN6 = "8319792839:AAGVDcJkyYi1AvQUwuRHnIuzQEiq4dhbZkA"
BOT_TOKEN7 = "8144493217:AAF_ITXpF63x3BZRHX1f28SZaeijgJz2MGw"
BOT_TOKEN8 = "8415072105:AAGHYz2elUhFhKIkbgWhluhBlnevCHaihNk"
BOT_TOKEN9 = "8236003776:AAFbIGo22m_HZ-Oerw5IkqRaEwCAmlrt-rM"
BOT_TOKEN10 = "8288517127:AAHHgW1dwNRmWLwnyMeO_vE0fZisdsQ4yOQ"

# Owner and Sudo users
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5518687442 7450385463 7998952043 7311297618").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8246711664"))
SUDO_USERS.append(OWNER_ID)

# Initialize only one active bot client
X1  = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2  = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3  = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4  = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5  = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6  = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7  = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8  = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9  = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)



