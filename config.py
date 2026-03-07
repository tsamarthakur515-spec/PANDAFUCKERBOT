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
BOT_TOKEN = "8565641545:AAFhiVi8tniZbu1S4OafKxLWQbbr-hzGRmk"
BOT_TOKEN2 = "8280409381:AAHJkHxjM7XwaZqKUvCSQPWXrkkMEN2faj4"
BOT_TOKEN3 = "8632280042:AAEZcLMxNtO-aBJlQ5JEEGY4ns5F3HtHB2c"
BOT_TOKEN4 = "7809825568:AAHYCYgel8EiKIm-zDzjsQvAxMSyj66mpQg"
BOT_TOKEN5 = "8795767972:AAGdBR-s1ZvY8Afh0zKJUFg6olQwBBFMqAk"
BOT_TOKEN6 = "8687100196:AAFwoX22dmcKDSTZ_h4LJczNkMFMWolJ7dM"
BOT_TOKEN7 = "8762340783:AAFZ99tg6K5a5eDQlxsYl9jr_-zQeuteBHY"
BOT_TOKEN8 = "8745619380:AAGjM8E4t8-PHREU73_MXz0gFr2tK3uz1RM"
BOT_TOKEN9 = "8600705453:AAHWLZ_jgFNQihbYlKRrpNWIvZyk2HUaOZI"
BOT_TOKEN10 = "8619853701:AAFEdz90PpDmUDlElO_h9tEjc7IjsxpF13U"

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



