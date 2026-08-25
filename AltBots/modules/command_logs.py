from os import getenv
import logging
from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

log = logging.getLogger("command_logs")

BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Prefer numeric group ID. Empty = logging disabled.
# Example: LOG_CHANNEL=-1004318913888
_raw = (getenv("LOG_CHANNEL") or "").strip()
if not _raw:
    LOG_CHANNEL = None
elif _raw.lstrip("-").isdigit():
    LOG_CHANNEL = int(_raw)
else:
    LOG_CHANNEL = _raw.lstrip("@")  # username without @

COMMAND_PREFIXES = ["/", "."]

# After first failure, stop retrying every command (spam logs)
_log_disabled = False


def attach_command_logger(bot):
    @bot.on(events.NewMessage)
    async def log_user_command(event):
        global _log_disabled

        if LOG_CHANNEL is None or _log_disabled:
            return

        try:
            sender = await event.get_sender()
        except Exception:
            return

        if not event.sender_id or getattr(sender, "bot", False):
            return

        message_text = event.raw_text or ""
        if not any(message_text.startswith(prefix) for prefix in COMMAND_PREFIXES):
            return

        try:
            user = sender
            chat = await event.get_chat()
            bot_info = await bot.get_me()

            log_message = (
                f"🟢 Command Used!\n"
                f"👤 User      : {getattr(user, 'first_name', '')}\n"
                f"💬 Username  : @{user.username if getattr(user, 'username', None) else 'N/A'}\n"
                f"🆔 User ID   : {user.id}\n"
                f"🏠 Chat      : {getattr(chat, 'title', None) or 'Private Chat'}\n"
                f"🤖 Bot       : {getattr(bot_info, 'first_name', '')}\n"
                f"📥 Command   : {message_text}"
            )
            await bot.send_message(LOG_CHANNEL, log_message)
        except Exception as e:
            # Invalid username / bot not in channel → disable further attempts
            _log_disabled = True
            log.warning(
                "LOG_CHANNEL failed (%s): %s — command logging disabled",
                LOG_CHANNEL,
                e,
            )


for bot in BOTS:
    attach_command_logger(bot)
