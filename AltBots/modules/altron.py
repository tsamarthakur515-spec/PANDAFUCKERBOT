import asyncio
from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# List of all bot clients
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Lines of console-style message
ALTRON_LINES = [
    "ɪɴɪᴛɪᴀʟɪᴢɪɴɢ... 🔵",
    "sʏsᴛᴇᴍ ʟᴏᴀᴅɪɴɢ:˹ᴀʀᴜ × ᴀᴘɪ˼ × [ʙᴏᴛs]",
    "ᴅᴇᴠᴇʟᴏᴘᴇʀ: ꯭ѕαмαя тнαкυя",
    "sᴛᴀᴛᴜs: Online ✅",
    "ᴍᴏᴅᴇ: ᴍᴜʟᴛɪ-ʙᴏᴛ ɪɴᴛᴇɢʀᴀᴛɪᴏɴ",
    "ᴘᴜʀᴘᴏsᴇ: ᴀᴜᴛᴏᴍᴀᴛᴇ | ᴍᴀɴᴀɢᴇ | ɪɴɴᴏᴠᴀᴛᴇ",
    "",
    "ᴀᴄᴄᴇss ɢʀᴀɴᴛᴇᴅ. ʙᴏᴛs ᴀʀᴇ ʟɪᴠᴇ & ᴇᴠᴏʟᴠɪɴɢ ⚙️",
    "sᴛᴀʏ ᴄᴏɴɴᴇᴄᴛᴇᴅ ғᴏʀ ɴᴇᴡ ʀᴇʟᴇᴀsᴇs & ᴜᴘᴅᴀᴛᴇs 🚀",
    "",
    "#ᴀʀᴜ #ʙᴏᴛs #sᴀᴍᴀʀ"
]

# Function to attach command to bot
def add_altron_command(bot):
    @bot.on(events.NewMessage(pattern="altron"))
    async def altron_info(event):
        chat_id = event.chat_id
        msg = await event.reply("`Initializing...`")  # send first line

        # Start editing message line by line
        current_text = ""
        for line in ALTRON_LINES:
            current_text += f"{line}\n"
            try:
                await msg.edit(f"```{current_text}```")
            except Exception as e:
                print(f"[EDIT ERROR] {e}")
            await asyncio.sleep(0.1)  # adjust speed of "typing"

# Attach to all bots
for bot in BOTS:
    add_altron_command(bot)
