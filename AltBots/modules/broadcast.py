import asyncio
from telethon import events, Button
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10

# --- Bots list ---
BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# --- Owner ID ---
OWNER_ID = 7724452546  # change to your Telegram ID

# --- Users and groups storage ---
USERS = set()
GROUPS = set()

# --- Save users/groups on every message ---
for bot in BOTS:
    @bot.on(events.NewMessage)
    async def save_users(event, bot=bot):
        if event.is_private:
            USERS.add(event.sender_id)
        elif event.is_group:
            GROUPS.add(event.chat_id)


# --- Broadcast functions ---
async def broadcast_to_users(reply):
    success = 0
    failed = 0
    tasks = []

    for user_id in USERS:
        for bot in BOTS:
            try:
                if reply.media:
                    tasks.append(bot.send_file(user_id, file=reply.media, caption=reply.text, buttons=reply.buttons))
                else:
                    tasks.append(bot.send_message(user_id, reply.text, buttons=reply.buttons))
            except Exception:
                failed += 1

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for res in results:
        if isinstance(res, Exception):
            failed += 1
        else:
            success += 1

    return success, failed, len(USERS)


async def broadcast_to_groups(reply):
    success = 0
    failed = 0
    tasks = []

    for group_id in GROUPS:
        for bot in BOTS:
            try:
                if reply.media:
                    tasks.append(bot.send_file(group_id, file=reply.media, caption=reply.text, buttons=reply.buttons))
                else:
                    tasks.append(bot.send_message(group_id, reply.text, buttons=reply.buttons))
            except Exception:
                failed += 1

    results = await asyncio.gather(*tasks, return_exceptions=True)
    for res in results:
        if isinstance(res, Exception):
            failed += 1
        else:
            success += 1

    return success, failed, len(GROUPS)


# --- Command handlers ---
for bot in BOTS:
    @bot.on(events.NewMessage(pattern=".ubroadcast"))
    async def user_broadcast(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("❌ You are not authorized to use this command.")

        reply = await event.get_reply_message()
        if not reply:
            return await event.reply("⚠️ Reply to a message (text/photo/video/buttons) to broadcast.")

        success, failed, total = await broadcast_to_users(reply)
        await event.reply(f"✅ User broadcast completed.\n\n📤 Sent: {success}\n❌ Failed: {failed}\n👤 Total users: {total}")


    @bot.on(events.NewMessage(pattern=".gbroadcast"))
    async def group_broadcast(event):
        if event.sender_id != OWNER_ID:
            return await event.reply("❌ You are not authorized to use this command.")

        reply = await event.get_reply_message()
        if not reply:
            return await event.reply("⚠️ Reply to a message (text/photo/video/buttons) to broadcast.")

        success, failed, total = await broadcast_to_groups(reply)
        await event.reply(f"✅ Group broadcast completed.\n\n📤 Sent: {success}\n❌ Failed: {failed}\n👥 Total groups: {total}")
