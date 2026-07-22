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
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="7724452546 7450385463 7998952043 7311297618").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="7724452546"))
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



