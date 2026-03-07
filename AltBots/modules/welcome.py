import random
import asyncio
from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# --- Bot clients ---
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# --- Random image links ---
WELCOME_IMAGES = [
    "https://files.catbox.moe/d8mnv9.jpg",
    "https://files.catbox.moe/4d7s4u.jpg",
    "https://files.catbox.moe/orqaah.jpg"
]

# --- Welcome message ---
WELCOME_TEXT = """🌸✨ ──────────────────── ✨🌸  
🎊 <b>ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ɢʀᴏᴜᴘ</b> 🎊  
  
🌹 <b>ɴᴀᴍᴇ</b> ➤ {name}  
🆔 <b>ᴜsᴇʀ ɪᴅ</b> ➤ <code>{user_id}</code>  
🏠 <b>ɢʀᴏᴜᴘ</b> ➤ {chat_title}  
  
💕 <b>ᴡᴇ'ʀᴇ sᴏ ʜᴀᴘᴘʏ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ʜᴇʀᴇ!</b>  
✨ <b>ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ sʜᴀʀᴇ ᴀɴᴅ ᴇɴᴊᴏʏ!</b>  
⚡ <b>ᴇɴᴊᴏʏ ʏᴏᴜʀ ᴇxᴘᴇʀɪᴇɴᴄᴇ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ</b>  
  
💝 <b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➤</b> <a href="https://t.me/sxyaru">˹ᴀʀᴜ × ᴀᴘɪ˼ × [ʙᴏᴛs]</a>  
🌸✨ ──────────────────── ✨🌸  
"""

# --- Buttons ---
WELCOME_BUTTONS = [
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/suruchisupport"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+fYnrOJSQP9I4ODlh")
    ]
]


# --- Handler for new members ---
async def welcome_user(event):
    if event.user_joined or event.user_added:
        try:
            user = await event.get_user()
            chat = await event.get_chat()
            name = user.first_name or "User"
            uid = user.id
            image = random.choice(WELCOME_IMAGES)
            caption = WELCOME_TEXT.format(name=name, user_id=uid, chat_title=chat.title)

            msg = await event.client.send_file(
                chat.id,
                image,
                caption=caption,
                buttons=WELCOME_BUTTONS,
                parse_mode="html"
            )

            # Auto delete after 60 seconds
            await asyncio.sleep(60)
            await msg.delete()
        except Exception as e:
            print(f"[WELCOME ERROR] {e}")


# --- Add handler for all bots ---
for bot in BOTS:
    bot.add_event_handler(welcome_user, events.ChatAction())
