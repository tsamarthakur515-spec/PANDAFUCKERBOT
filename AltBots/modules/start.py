from telethon import __version__, events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

START_BUTTON = [
    [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/+4eTddUofQDlkYjhl"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/suruchi_network")
    ],
    [Button.inline("• ʀᴇᴘᴏ •", data="repo")]
]

# List of all bot clients
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

async def start_handler(event):
    AltBot = await event.client.get_me()
    bot_name = AltBot.first_name
    bot_id = AltBot.id
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}]\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [꯭𐏓꯭🇳🇵꯭𐏓꯭ 𝐀꯭𝛅 ꯭ꭙ ꯭ᯓ꯭𓆰𝅃꯭᳚ ⃪ ⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠༎ ꯭𝐒꯭𝛂꯭𝐦꯭𝐚𝐫 ꯭꯭𝆺꯭𝅥༎ࠫ𐏓꯭꯭𝅥🍃꯭](tg://openmessage?user_id=7724452546)**\n\n"
    TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
    TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"

    await event.client.send_file(
        event.chat_id,
        "https://t.me/BOM_BOM68/965",
        caption=TEXT,
        buttons=START_BUTTON
    )

async def button_handler(event):
    # event.data is bytes, so decode if needed
    data = event.data.decode("utf-8")
    
    if data == "repo":
        await event.answer(
            "𝐁𝐇𝐀𝐆 𝐉𝐇𝐀 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐃 𝐑𝐄𝐏𝐎 𝐊𝐘𝐀 𝐋𝐀𝐆𝐀 𝐒𝐀𝐌𝐀𝐑 𝐓𝐇𝐀𝐊𝐔𝐑 𝐊𝐀 𝐋𝐀𝐍𝐃 𝐋𝐄𝐋𝐄 👿\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ˹ᴀʀᴜ × ᴀᴘɪ˼ × [ʙᴏᴛs]",
            alert=True
        )

# Attach to all bots
for bot in BOTS:
    bot.add_event_handler(button_handler, events.CallbackQuery)


# --- Callback for "Back" Button ---

# Attach the same /start handler to all bots
for bot in BOTS:
    bot.add_event_handler(start_handler, events.NewMessage(pattern="/start"))
