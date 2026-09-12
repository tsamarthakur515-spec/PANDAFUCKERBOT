from telethon import events
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10
import asyncio
import random

BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

@events.register(events.NewMessage(pattern=r"\.tagall"))
async def tag_all_handler(event):
    if not event.is_group:
        return await event.reply("❌ This command only works in groups")

    # Optional custom message
    msg = event.text.split(" ", 1)
    message = msg[1] if len(msg) > 1 else "🛍️ Tagging everyone!"

    mentions = []
    async for user in event.client.iter_participants(event.chat_id):
        if user.bot:
            continue
        if user.first_name:
            mentions.append(f"[{user.first_name}]")

    BATCH_SIZE = 20
    total = len(mentions)
    count = 0

    for i in range(0, total, BATCH_SIZE):
        batch = mentions[i:i + BATCH_SIZE]
        text = f"{message}\n\n" + " ".join(batch)
        try:
            await event.client.send_message(event.chat_id, text)
            count += len(batch)
            await asyncio.sleep(random.uniform(3.0, 5.0))  # Safe delay
        except Exception as e:
            print(f"[TAGALL ERROR] {e}")

    await event.reply(f"✅ Successfully tagged {count} members!")


# Attach to all bots
for bot in BOTS:
    bot.add_event_handler(tag_all_handler)