from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# All bot clients
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Channel or group to send logs
LOG_CHANNEL = "@bot_testing_by_panda_and_samar"  # Replace with your channel username or ID

# Command prefixes your bots use
COMMAND_PREFIXES = ["/", "."]  # Add more if needed

def attach_command_logger(bot):
    @bot.on(events.NewMessage)
    async def log_user_command(event):
        if event.sender_id and not (await event.get_sender()).bot:
            message_text = event.raw_text or ""
            
            # Only log messages that start with a command prefix
            if not any(message_text.startswith(prefix) for prefix in COMMAND_PREFIXES):
                return  # Ignore non-command messages

            user = await event.get_sender()
            chat = await event.get_chat()
            bot_info = await bot.get_me()

            log_message = f"""
🟢 Command Used!
👤 User      : {user.first_name}
💬 Username  : @{user.username if user.username else 'N/A'}
🆔 User ID   : {user.id}
🏠 Chat      : {chat.title if hasattr(chat, 'title') else 'Private Chat'}
🤖 Bot       : {bot_info.first_name}
📥 Command   : {message_text}
"""
            await bot.send_message(LOG_CHANNEL, log_message)

# Attach logger to all bots
for bot in BOTS:
    attach_command_logger(bot)
