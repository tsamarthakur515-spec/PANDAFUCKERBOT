import sys
from os import execl
from telethon import events
from datetime import datetime
from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10,
    OWNER_ID, SUDO_USERS, CMD_HNDLR as hl
)

ALL_BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]


async def _persist_sudo():
    """Persist current SUDO_USERS to DB so it survives a restart."""
    try:
        from AltBots.db import save_sudoers

        ok = await save_sudoers(list(SUDO_USERS), OWNER_ID)
        return ok
    except Exception:
        return False


# Ping Command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}ping(?: |$)(.*)"))
    async def ping(e):
        if e.sender_id not in SUDO_USERS:
            await e.reply("⛔ You are not authorized to use this command.")
            return

        start = datetime.now()
        reply = await e.reply("🏓 Pinging...")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await reply.edit(f"🏓 **Pong!**\n⏱ Response time: `{ms:.2f} ms`")


# Reboot Command
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}reboot(?: |$)(.*)"))
    async def reboot(e):
        if e.sender_id not in SUDO_USERS:
            await e.reply("⛔ You are not authorized to use this command.")
            return

        await e.reply("🔄 Restarting the bot, please wait...")
        # Use e.client — NOT the loop variable `bot` (closure bug)
        try:
            await e.client.disconnect()
        except Exception:
            pass
        execl(sys.executable, sys.executable, *sys.argv)


# Add Sudo User
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudo(?: |$)(.*)"))
    async def add_sudo(event):
        if event.sender_id != OWNER_ID:
            await event.reply("⛔ Only the bot owner can grant sudo access.")
            return

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            await event.reply("⚠️ Reply to a user's message to grant them sudo access.")
            return

        target = int(reply_msg.sender_id)
        if target in SUDO_USERS:
            await event.reply("ℹ️ This user already has sudo access.")
            return

        SUDO_USERS.append(target)
        saved = await _persist_sudo()
        status = "saved to DB" if saved else "memory only, DB save failed"
        await event.reply(f"✅ Sudo access granted to `{target}` ({status}).")


# Remove Sudo User
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}rmsudo(?: |$)(.*)"))
    async def remove_sudo(event):
        if event.sender_id != OWNER_ID:
            await event.reply("⛔ Only the bot owner can revoke sudo access.")
            return

        reply_msg = await event.get_reply_message()
        if not reply_msg:
            await event.reply("⚠️ Reply to a user's message to revoke their sudo access.")
            return

        target = int(reply_msg.sender_id)
        if target == int(OWNER_ID):
            await event.reply("⛔ The owner's sudo access cannot be removed.")
            return

        if target not in SUDO_USERS:
            await event.reply("⚠️ This user does not have sudo access.")
            return

        SUDO_USERS.remove(target)
        saved = await _persist_sudo()
        status = "saved to DB" if saved else "memory only, DB save failed"
        await event.reply(f"✅ Sudo access revoked for `{target}` ({status}).")


# Show Sudo List
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=rf"\{hl}sudolist(?: |$)(.*)"))
    async def sudo_list(event):
        if event.sender_id not in SUDO_USERS:
            await event.reply("⛔ You are not authorized to use this command.")
            return

        if not SUDO_USERS:
            await event.reply("ℹ️ No sudo users have been added yet.")
            return

        text = "**Active Sudo Users:**\n\n"
        for i, user_id in enumerate(SUDO_USERS, 1):
            text += f"{i}. `{user_id}`\n"
        await event.reply(text)
