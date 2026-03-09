import sys
from os import execl, getenv
from telethon import events
from datetime import datetime
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    OWNER_ID, SUDO_USERS, CMD_HNDLR as hl
)

ALL_BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]


# ✅ Ping Command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}ping(?: |$)(.*)"))
    async def ping(e):
        if e.sender_id in SUDO_USERS:
            start = datetime.now()
            reply = await e.reply("» __˹ᴀʀᴜ × ᴀᴘɪ˼ × [ʙᴏᴛs]__")
            end = datetime.now()
            ms = (end - start).microseconds / 1000
            await reply.edit(f"`🤖 ᴘɪɴɢ\n» sᴀᴍᴀʀ ᴛʜᴀᴋᴜʀ ραρα нєяє αв кιѕкι ᴍᴀᴀ ᴄʜᴏᴅᴜ {ms} ᴍꜱ`")
        else:
            await e.reply("» ᴘʜᴀʟᴇ sᴀᴍᴀʀ ᴘᴀᴘᴀ sᴀ sᴜᴅᴏ ʟᴇʟᴇ ʙᴋʟ 👿 ")


# 🔁 Reboot Command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}reboot(?: |$)(.*)"))
    async def reboot(e):
        if e.sender_id in SUDO_USERS:
            await e.reply("`sᴀᴍᴀʀ ᴘᴀᴘᴀ ᴋᴀ ᴄᴏᴍᴇʙᴀᴄᴋ ʜᴏ ɢʏᴀ ʙᴀᴄᴄʜᴇ 😈`")
            await bot.disconnect()
            execl(sys.executable, sys.executable, *sys.argv)
        else:
            await e.reply("» ᴘʜᴀʟᴇ sᴀᴍᴀʀ ᴘᴀᴘᴀ sᴀ sᴜᴅᴏ ʟᴇʟᴇ ʙᴋʟ 👿")


# 🧑‍💻 Add Sudo User
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudo(?: |$)(.*)"))
    async def add_sudo(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("» ʙʜᴀᴋ ᴍᴀᴅᴇʀᴄʜᴏᴅ ᴛᴜ sᴜᴅᴏ ᴏᴡɴᴇʀ ɴᴀʜɪ ʜᴀɪ ❌")

        ok = await event.reply("» sᴀᴍᴀʀ ᴘᴀᴘᴀ ɴᴇ sᴜᴅᴏ ᴅᴇ ᴅᴇʏᴀ ᴀʙ ʜᴀᴛᴇʀs ᴋɪ ᴄʜᴜᴅᴀɪ sʜᴜʀᴜ ᴋᴀʀ 🥵 ")

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            return await ok.edit("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴛᴏ ᴀᴅᴅ ᴀs sᴜᴅᴏ !!")

        target = reply_msg.sender_id
        if target in SUDO_USERS:
            return await ok.edit("» ᴛᴜ ᴀʟʀᴇᴀᴅʏ sᴜᴅᴏ ʜᴀɪ   ✅")

        SUDO_USERS.append(int(target))
        await ok.edit(f"» **sᴀᴍᴀʀ ᴘᴀᴘᴀ ɴᴇ ᴛᴜᴊʜᴇ sᴜᴅᴏ ᴅᴇ ᴅᴇʏᴀ ʜᴀɪ ᴀʙ ʜᴀᴛᴇʀs ᴋɪ ᴍᴀᴀ ᴄʜᴏᴅɴᴀ sʜᴜʀᴜ ᴋᴀʀ 🥵 ** `{target}`")


# 🚫 Remove Sudo User
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}rmsudo(?: |$)(.*)"))
    async def remove_sudo(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("» ʙʜᴀᴋ ᴍᴀᴅᴇʀᴄʜᴏᴅ ᴛᴜ sᴜᴅᴏ ᴏᴡɴᴇʀ ɴᴀʜɪ ʜᴀɪ 🤣")

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            return await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇᴍ ғʀᴏᴍ sᴜᴅᴏ")

        target = reply_msg.sender_id
        if target not in SUDO_USERS:
            return await event.reply("» ᴜsᴇʀ ɴᴏᴛ ɪɴ sᴜᴅᴏ ʟɪsᴛ ❌")

        SUDO_USERS.remove(int(target))
        await event.reply(f"» **ʀᴇᴍᴏᴠᴇᴅ ғʀᴏᴍ sᴜᴅᴏ:** `{target}` ✅")


# 📜 Show Sudo List
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudolist(?: |$)(.*)"))
    async def sudo_list(event):
        if not SUDO_USERS:
            return await event.reply("» ɴᴏ sᴜᴅᴏ ᴜsᴇʀs ᴀᴅᴅᴇᴅ ʏᴇᴛ ❌")

        text = "» **ᴀᴄᴛɪᴠᴇ sᴜᴅᴏ ᴜsᴇʀs:**\n\n"
        for i, user_id in enumerate(SUDO_USERS, 1):
            text += f"**{i}.** `{user_id}`\n"
        await event.reply(text)
