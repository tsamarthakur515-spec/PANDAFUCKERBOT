import random
import asyncio
from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# --- Bot clients ---
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# --- Premium Welcome Images (Catbox)
WELCOME_IMAGES = [
    "https://files.catbox.moe/d8mnv9.jpg",
    "https://files.catbox.moe/4d7s4u.jpg",
    "https://files.catbox.moe/orqaah.jpg",
    "https://files.catbox.moe/4d7s4u.jpg",
    "https://files.catbox.moe/d8mnv9.jpg",
]

# --- ULTRA BEAUTIFUL WELCOME MESSAGE ---
WELCOME_TEXT = """🌟✨ **🌈 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴇᴍᴘᴇʀᴏʀ ᴄᴏᴍᴍᴜɴɪᴛʏ 🌈** ✨🌟

🎉 <b>Hey {name}!</b> 🎉

📖 <b>Your ID:</b> <code>{user_id}</code>
🏠 <b>Group:</b> {chat_title}

💖 <b>Wishing you a warm welcome!</b>  
✨ <b>Enjoy every moment with your new friends</b>  
⚡ <b>Powered by <a href="https://t.me/sxyaru">sxyaru × Aru × Bots</a></b>

🌟 <b>Tag someone & share the joy!</b>  
🌸 Feel free to explore and have fun here! 🌸"""

# --- Stylish Buttons ---
WELCOME_BUTTONS = [
    [
        Button.url("📢 Channel", "https://t.me/+kycml-zhzSs2Zjdl"),
        Button.url("💬 Support", "https://t.me/+qwlkJNntCU0yMjhl")
    ],
    [
        Button.url("🌟 Join Channel", "https://t.me/+kycml-zhzSs2Zjdl"),
        Button.url("🤝 Invite Friends", "https://t.me/+kycml-zhzSs2Zjdl")
    ]
]


# --- Handler ---
async def welcome_user(event):
    if not (event.user_joined or event.user_added):
        return

    try:
        user = await event.get_user()
        chat = await event.get_chat()

        name = user.first_name or "Friend"
        uid = user.id
        image = random.choice(WELCOME_IMAGES)
        caption = WELCOME_TEXT.format(
            name=name, user_id=uid, chat_title=chat.title
        )

        msg = await event.client.send_file(
            chat.id,
            image,
            caption=caption,
            buttons=WELCOME_BUTTONS,
            parse_mode="html"
        )

        # Auto delete after 40 seconds
        await asyncio.sleep(40)
        await msg.delete()

    except Exception as e:
        print(f"[WELCOME ERROR] {e}")


# --- Add to all bots ---
for bot in BOTS:
    bot.add_event_handler(welcome_user, events.ChatAction())