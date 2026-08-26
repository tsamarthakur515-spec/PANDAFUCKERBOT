import asyncio
import re
from random import choice, sample

from telethon import events
from telethon.tl.types import MessageEntityCustomEmoji, MessageEntityTextUrl

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID

REPLY_RAID = []
ALL_BOTS = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

CUSTOM_EMOJI_IDS = [
    6334515684252326433, 6334763787333147638, 6334761725748846498, 6334586375119051935,
    6093398638321475389, 6096083263464415963, 6095713346521144919, 6095988580910375034,
    6095706693616804285, 6095657735284597191, 6096183323317509438, 6096183529475941311,
    6095949445168373144, 6096035241435078733, 6095675529334103687, 6095785278633418890,
    6096043444822614389, 6093522294724894291, 6096167105521000703, 6093861605731212875,
    6096054628917453455, 6096115686172532857, 6095961561271115744, 6096148035866206608,
    6096132385005379427, 6095865345413751303, 6098136309371509564, 6095724491961277782,
    6095893559053917535, 6096022665770835861, 6098201124722974324, 6095825479527309554,
    6095803201531945360, 6095903484723338612, 6098260846243224336, 6098069329356528539,
    6095659659429945869, 6098091358243789738, 6095830702207541814, 6097888588542779911,
    6095902496880861629, 6095650519739538680, 6095675580873711995, 6095673905836466207,
    6095664903585014100, 6098155413386042411, 6095740026857988145, 6096064090730405777,
    6291780433239614475, 6291978834958886683,
]


def two_premium_emojis():
    ids = sample(CUSTOM_EMOJI_IDS, 2)
    base = "\u2060"
    text = base + base + " "
    entities = [
        MessageEntityCustomEmoji(offset=0, length=1, document_id=ids[0]),
        MessageEntityCustomEmoji(offset=1, length=1, document_id=ids[1]),
    ]
    return text, entities


async def send_with_premium_emojis(client, chat_id, body, reply_to=None, mention_name=None, mention_id=None):
    prefix, ents = two_premium_emojis()
    if mention_name and mention_id:
        name = (mention_name or "User").strip() or "User"
        full_text = prefix + name + " " + body
        ents.append(MessageEntityTextUrl(offset=3, length=len(name), url=f"tg://user?id={mention_id}"))
        text = full_text
    else:
        text = prefix + body
    kwargs = {"formatting_entities": ents}
    if reply_to is not None:
        kwargs["reply_to"] = reply_to
    await client.send_message(chat_id, text, **kwargs)


async def _do_raid(e, raid_list, cmd_name):
    if e.sender_id not in SUDO_USERS:
        return
    text = e.text or ""
    args = re.sub(rf"^[./]{cmd_name}(?:@\w+)?\s*", "", text, flags=re.IGNORECASE).strip()
    parts = args.split(maxsplit=1)
    try:
        if not parts:
            await e.reply(f"**Usage:**\n`{hl}{cmd_name} <count> <username>`\n`{hl}{cmd_name} <count>` (reply to user)")
            return
        counter = int(parts[0])
        if len(parts) >= 2:
            entity = await e.client.get_entity(parts[1])
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
        else:
            await e.reply(f"**Usage:**\n`{hl}{cmd_name} <count> <username>`\n`{hl}{cmd_name} <count>` (reply to user)")
            return

        uid = entity.id
        if uid in ALTRON or uid == OWNER_ID or uid in SUDO_USERS:
            await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ.")
            return

        first_name = (entity.first_name or "User").strip() or "User"
        for _ in range(counter):
            reply = choice(raid_list)
            await send_with_premium_emojis(e.client, e.chat_id, reply, mention_name=first_name, mention_id=uid)
            await asyncio.sleep(0.1)
    except ValueError:
        await e.reply("Count number hona chahiye. Example: `.raid 5 @user`")
    except Exception as err:
        await e.reply(f"Error: `{str(err)[:200]}`")
        print(err)


# ========== RAID ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=r"^[./]raid(?:@\w+)?(?: |$)(.*)"))
    async def raid_handler(e):
        await _do_raid(e, RAID, "raid")

# ========== MRAID ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=r"^[./]mraid(?:@\w+)?(?: |$)(.*)"))
    async def mraid_handler(e):
        await _do_raid(e, MRAID, "mraid")

# ========== SRAID ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=r"^[./]sraid(?:@\w+)?(?: |$)(.*)"))
    async def sraid_handler(e):
        await _do_raid(e, SRAID, "sraid")

# ========== CRAID ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=r"^[./]craid(?:@\w+)?(?: |$)(.*)"))
    async def craid_handler(e):
        await _do_raid(e, CRAID, "craid")

# ========== REPLY RAID ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True))
    async def reply_raid_listener(event):
        global REPLY_RAID
        check = f"{event.sender_id}_{event.chat_id}"
        if check in REPLY_RAID:
            body = choice(REPLYRAID)
            await send_with_premium_emojis(event.client, event.chat_id, body, reply_to=event.message.id)

# ========== RRAID (start reply raid) ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
    async def rraid_handler(e):
        if e.sender_id not in SUDO_USERS:
            return
        try:
            if e.reply_to_msg_id:
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
            else:
                arg = re.sub(r"^[./]rraid(?:@\w+)?\s*", "", e.text or "", flags=re.IGNORECASE).strip()
                if not arg:
                    await e.reply(f"**Usage:** `{hl}rraid @user` ya reply karke")
                    return
                entity = await e.client.get_entity(arg)

            user_id = entity.id
            if user_id in ALTRON or user_id == OWNER_ID or user_id in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ.")
                return

            global REPLY_RAID
            check = f"{user_id}_{e.chat_id}"
            if check not in REPLY_RAID:
                REPLY_RAID.append(check)
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ғᴜᴄᴋɪɴɢ sᴛᴀʀᴛ ✅")
        except Exception as err:
            await e.reply(f"Error: `{str(err)[:150]}`")

# ========== DRRAID (stop reply raid) ==========
for bot in ALL_BOTS:
    @bot.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
    async def drraid_handler(e):
        if e.sender_id not in SUDO_USERS:
            return
        try:
            if e.reply_to_msg_id:
                a = await e.get_reply_message()
                entity = await e.client.get_entity(a.sender_id)
            else:
                arg = re.sub(r"^[./]drraid(?:@\w+)?\s*", "", e.text or "", flags=re.IGNORECASE).strip()
                if not arg:
                    await e.reply(f"**Usage:** `{hl}drraid @user` ya reply karke")
                    return
                entity = await e.client.get_entity(arg)

            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ғᴜᴄᴋɪɴɢ sᴛᴏᴘ ✅")
        except Exception as err:
            await e.reply(f"Error: `{str(err)[:150]}`")
