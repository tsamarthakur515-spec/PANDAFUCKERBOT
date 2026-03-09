from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl

# All bot clients
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Start buttons (used in back_to_start)
START_BUTTON = [
    [Button.inline("• ꜱᴘᴀᴍ •", data="spam"), Button.inline("• ʀᴀɪᴅ •", data="raid")],
    [Button.inline("• ᴇxᴛʀᴀ •", data="extra")],
    [
        Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/suruchisupport"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+fYnrOJSQP9I4ODlh")
    ],
    [Button.inline("• ʙᴀᴄᴋ •", data="back_start")]
]

HELP_STRING = f"★ ꯭𐏓꯭🇳🇵꯭𐏓꯭ 𝐀꯭𝛅 ꯭ꭙ ꯭ᯓ꯭𓆰𝅃꯭᳚ ⃪ ⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠༎ ꯭𝐒꯭𝛂꯭𝐦꯭𝐚𝐫 ꯭꯭𝆺꯭𝅥༎ࠫ𐏓꯭꯭𝅥🍃꯭ 𝒉𝒆𝒍𝒑𝒎𝒆𝒏𝒖 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ll_Sexcy_Samar_ll**"

# Messages for different categories
extra_msg = f"""
**» ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ**
  1) {hl}ping 
  2) {hl}reboot
  3) {hl}sudo <reply to user>  --> Owner Cmd
  4) {hl}logs --> Owner Cmd

𝗘𝗰𝗵𝗼: **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ**
  1) {hl}echo <reply to user>
  2) {hl}rmecho <reply to user>

𝗟𝗲𝗮𝘃𝗲: **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ**
  1) {hl}leave <group/chat id>
  2) {hl}leave : Type in the Group bot will auto leave that group

**© @LUL**
"""

raid_msg = f"""
**» ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ.**
  1) {hl}raid <count> <username>
  2) {hl}raid <count> <reply to user>

𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}rraid <replying to user>
  2) {hl}rraid <username>

𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}drraid <replying to user>
  2) {hl}drraid <username>

𝐌𝐑𝐚𝐢𝐝: **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}mraid <count> <username>
  2) {hl}mraid <count> <reply to user>

𝐒𝐑𝐚𝐢𝐝: **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ.**
  1) {hl}sraid <count> <username>
  2) {hl}sraid <count> <reply to user>

𝐂𝐑𝐚𝐢𝐝: **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴜꜱᴇʀ.**
  1) {hl}craid <count> <username>
  2) {hl}craid <count> <reply to user>

**© @LUL**
"""

spam_msg = f"""
**» ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ:**

𝗦𝗽𝗮𝗺: **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ.**
  1) {hl}spam <count> <message to spam> (reply any message to spam that)
  2) {hl}spam <count> <replying any message>

𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ.**
  1) {hl}pspam <count>

𝗛𝗮𝗻𝗴: **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ.**
  1) {hl}hang <counter>

**© @SXYARU**
"""

async def button_handler(event):
    # event.data is bytes, so decode if needed
    data = event.data.decode("utf-8")
    
    if data == "repo":
        await event.answer(
            "𝐁𝐇𝐀𝐆 𝐌𝐀𝐃𝐄𝐑𝐂𝐇𝐎𝐃 𝐑𝐄𝐏𝐎 𝐊𝐘𝐀 𝐋𝐄𝐆𝐀 𝐈𝐒𝐀𝐒𝐀 𝐀𝐀𝐂𝐇𝐀 𝐒𝐀𝐌𝐀𝐑 𝐏𝐀𝐏𝐀 𝐊𝐀 𝐋𝐀𝐍𝐃 𝐋𝐄𝐋𝐄 🤣\n\n ᴘᴏᴡᴇʀᴇᴅ ʙʏ ˹ᴀʀᴜ × ᴀᴘɪ˼ × [ʙᴏᴛs]",
            alert=True
        )

# Attach to all bots
for bot in BOTS:
    bot.add_event_handler(button_handler, events.CallbackQuery)

# ---------------- Handlers ----------------

async def send_help(event):
    if event.sender_id in SUDO_USERS:
        try:
            await event.client.send_file(
                event.chat_id,
                "https://t.me/BOM_BOM68/965",
                caption=HELP_STRING,
                buttons=START_BUTTON
            )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occurred!\n\n**ERROR:** {str(e)}")

async def handle_callback(event):
    user_id = event.query.user_id
    if user_id not in SUDO_USERS:
        await event.answer("Make Your Own Altron Bots !! @LUL", cache_time=0, alert=True)
        return

    pattern = event.data.decode("utf-8")
    if pattern == "help_back":
        await event.edit(HELP_STRING, buttons=START_BUTTON)
    elif pattern == "spam":
        await event.edit(spam_msg, buttons=[[Button.inline("• ʙᴀᴄᴋ •", data="help_back")]])
    elif pattern == "raid":
        await event.edit(raid_msg, buttons=[[Button.inline("• ʙᴀᴄᴋ •", data="help_back")]])
    elif pattern == "extra":
        await event.edit(extra_msg, buttons=[[Button.inline("• ʙᴀᴄᴋ •", data="help_back")]])

async def back_to_start(event):
    AltBot = await event.client.get_me()
    bot_name = AltBot.first_name
    bot_id = AltBot.id

    # Custom message
    TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}]\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
    TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [ ꯭𐏓꯭🇳🇵꯭𐏓꯭ 𝐀꯭𝛅 ꯭ꭙ ꯭ᯓ꯭𓆰𝅃꯭᳚ ⃪ ⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠༎ ꯭𝐒꯭𝛂꯭𝐦꯭𝐚𝐫 ꯭꯭𝆺꯭𝅥༎ࠫ𐏓꯭꯭𝅥🍃꯭ ](tg://openmessage?user_id=7724452546)**\n\n"
    TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3\n`"
    TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3\n`"
    TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `1.41.2\n`━━━━━━━━━━━━━━━━━"

    # Custom buttons layout
    CUSTOM_BUTTONS = [
        [Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")],
        [
            Button.url("• ᴄʜᴀɴɴᴇʟ •", "https://t.me/suruchisupport"),
            Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/+fYnrOJSQP9I4ODlh")
        ],
        [Button.inline("• ʀᴇᴘᴏ •", data="repo")]
    ]

    await event.edit(TEXT, buttons=CUSTOM_BUTTONS)

# ---------------- Attach handlers to all bots ----------------

for bot in BOTS:
    bot.add_event_handler(send_help, events.NewMessage(incoming=True, pattern=fr"\{hl}help(?: |$)(.*)"))
    bot.add_event_handler(handle_callback, events.CallbackQuery)
    bot.add_event_handler(back_to_start, events.CallbackQuery(data=b"back_start"))

