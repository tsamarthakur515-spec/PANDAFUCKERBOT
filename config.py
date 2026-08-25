import logging
from os import getenv
from telethon import TelegramClient
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

# Bot tokens
BOT_TOKEN = "8711056379:AAF5RcXoprTIAcQWDgKpbDxSC1WllcKaPOY"
BOT_TOKEN2 = "8907901853:AAESldCj5IVymic3IT7VSv0gPROePgpxcNE"
BOT_TOKEN3 = "8862433888:AAEvXmtDYZY8OhL5rrz8lzVo3ai8tc29vRY"
BOT_TOKEN4 = "8509012033:AAHEztfHEh6ZB_jHCFukaHTYiK6g1KjDlPc"
BOT_TOKEN5 = "8971116678:AAFQRZBl-kDmAeGFuPYvww26WkDG46ntis8"
BOT_TOKEN6 = "8766121545:AAEB_c2jlrLkrAKERgiMDwwsllFAjtvgR2M"
BOT_TOKEN7 = "8596765113:AAFazQtC_p7rSJ55ThvaSgVytA5BMgTELqs"
BOT_TOKEN8 = "8932132745:AAGuF12Jo5_v0AoKiVwz55liOSUIZ4S0n7E"
BOT_TOKEN9 = "8848139467:AAHtGeoJkaOOeSJWxS0t4xOzP5ENZY90k1I"
BOT_TOKEN10 = "7595711008:AAFL4Svub5B2mHgPrFUFl0i6LKapzkGr1Ng"

# Keep all tokens in a list so the rest of the code can reference them.
BOT_TOKENS = [
    BOT_TOKEN, BOT_TOKEN2, BOT_TOKEN3, BOT_TOKEN4, BOT_TOKEN5,
    BOT_TOKEN6, BOT_TOKEN7, BOT_TOKEN8, BOT_TOKEN9, BOT_TOKEN10
]

# Owner and Sudo users
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8841848847").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8841848847"))
SUDO_USERS.append(OWNER_ID)

# How many bots to start by default
ACTIVE_BOT_COUNT = int(getenv("ACTIVE_BOT_COUNT", "10"))

# Optionally set START_ALL=true to attempt to start all tokens
START_ALL = getenv("START_ALL", "true").lower() in ("1", "true", "yes")

# Container for started client objects — populated by main.py's async main()
clients = {}

# Create TelegramClient objects for X1..X10 so modules can register handlers on them.
# NOTE: Clients are NOT started here — starting is done inside main.py's async main()
# so the clients live on the correct persistent event loop.
for i in range(1, 11):
    name = f"X{i}"
    globals()[name] = TelegramClient(name, API_ID, API_HASH)
