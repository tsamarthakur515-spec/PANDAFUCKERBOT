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
API_ID = int(getenv("API_ID", "0"))
API_HASH = getenv("API_HASH", "")
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

# Bot tokens - ONLY from environment variables (never hardcode tokens)
BOT_TOKEN = getenv("BOT_TOKEN", "8589306606:AAErnpkrJhlynLcUWA8ebIz4tU8kcmeLmrk")
BOT_TOKEN2 = getenv("BOT_TOKEN2", "8877968647:AAHQdpWtNZXomMm1k9X2Ud1fY5Ogd7feQIc")
BOT_TOKEN3 = getenv("BOT_TOKEN3", "8940478013:AAHmNFIpOpAZBgErEM-Z3nmtwmUQ6wanebU")
BOT_TOKEN4 = getenv("BOT_TOKEN4", "8948145043:AAFma_IBiRibTqtN8jd44gzuM5s68AM6Mvo")
BOT_TOKEN5 = getenv("BOT_TOKEN5", "8608799874:AAEokZuThirnAEvWKGpG3SYlxRZnWJR0KW0")
BOT_TOKEN6 = getenv("BOT_TOKEN6", "8800142370:AAF9lWZkc9rCDw0lgyo8nfsPbpRcvOgzVGQ")
BOT_TOKEN7 = getenv("BOT_TOKEN7", "8941098522:AAGbsebaUR4RYZ3ngpzyedgS9f_YXnkqtr0")
BOT_TOKEN8 = getenv("BOT_TOKEN8", "8852131218:AAFcPwUPc2Q63GxXNdi9gHibDHRZjB9T3vk")
BOT_TOKEN9 = getenv("BOT_TOKEN9", "8963620107:AAF7ma1XSZ4ey3I2lncDhOcPsEbyefVyOyU")
BOT_TOKEN10 = getenv("BOT_TOKEN10", "8549782429:AAEVeI1Nf6OmTVuZ7Gul14vDyGW58OFWQPs")

# Keep all tokens in a list (empty strings will be skipped later)
BOT_TOKENS = [
    BOT_TOKEN, BOT_TOKEN2, BOT_TOKEN3, BOT_TOKEN4, BOT_TOKEN5,
    BOT_TOKEN6, BOT_TOKEN7, BOT_TOKEN8, BOT_TOKEN9, BOT_TOKEN10
]
# Remove empty tokens
BOT_TOKENS = [t for t in BOT_TOKENS if t and t.strip()]

# Owner and Sudo users
SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="8841848847").split()))
for x in ALTRON:
    if x not in SUDO_USERS:
        SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="8841848847"))
if OWNER_ID not in SUDO_USERS:
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
