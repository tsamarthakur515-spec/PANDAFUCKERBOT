from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10
from telethon import __version__

BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# ==================== START BUTTONS ====================
START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/+kycml-zhzSs2Zjdl"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+qwlkJNntCU0yMjhl")
    ],
    [Button.inline("• ʀᴇᴘᴏ •", data="repo")]
]

# ==================== ULTRA PRO START TEXT ====================
TEXT = """🌟✨ **🌟 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ 🌟** ✨🌟

🎉 <b>Hey [{event.sender.first_name}]!</b> 🎉

I am <a href="tg://user?id={bot_id}">{bot_name}</a>

━━━━━━━━━━━━━━━━━━━
👑 <b>Developer:</b> [꯭‌𝅃꯭꯭꯭᳚ ꯭𓆰꯭꯭🍃꯭♔꯭𝐑꯭𝛕꯭꯭֟ؖ۬፝𝛅༭꯭𝐉ᴀ꯭ᴍ꯭፝֟፝֟ᴇ꯭s꯭𝄢꯭|꯭🔥꯭꯭➛](tg://openmessage?user_id=8841848847)
📱 <b>xBots Version:</b> <code>M3.3</code>
🐍 <b>Python Version:</b> <code>3.11.3</code>
🤖 <b>Telethon Version:</b> <code>{__version__}</code>
━━━━━━━━━━━━━━━━━━━

💥 <b>Tagall</b> • <b>Welcome</b> • <b>Moderation</b> • <b>Fun Commands</b> • <b>NSFW</b> • <b>Games</b>

🌸 Feel free to explore & enjoy with us! 🌸"""

# ==================== VIDEO (ya image) ====================
VIDEO_URL = "https://files.catbox.moe/q7ng03.mp4"   # Change karna agar chahiye


async def start_handler(event):
    AltBot = await event.client.get_me()
    bot_name = AltBot.first_name
    bot_id = AltBot.id

    caption = TEXT.format(
        event.sender.first_name=event.sender.first_name or "Friend",
        bot_name=bot_name,
        bot_id=bot_id,
        __version__=__version__
    )

    await event.client.send_file(
        event.chat_id,
        VIDEO_URL,
        caption=caption,
        buttons=START_BUTTON,
        parse_mode="html",
        supports_streaming=True
    )


async def button_handler(event):
    data = event.data.decode("utf-8")

    if data == "repo":
        await event.answer(
            "Bhag ja bheekhari, khud se bana le repo 😐\n\nPowered by sxyaru × Aru × Bots",
            alert=True
        )


# ==================== ATTACH TO ALL BOTS ====================
for bot in BOTS:
    bot.add_event_handler(button_handler, events.CallbackQuery)

for bot in BOTS:
    bot.add_event_handler(start_handler, events.NewMessage(pattern="/start"))