import asyncio
from random import choice, sample

from telethon import events
from telethon.tl.types import MessageEntityCustomEmoji

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, OWNER_ID, CMD_HNDLR as hl
from AltBots.data import RAID, REPLYRAID, ALTRON, MRAID, SRAID, CRAID

REPLY_RAID = []

# Premium custom emoji document IDs only
CUSTOM_EMOJI_IDS = [
    6334515684252326433,
    6334763787333147638,
    6334761725748846498,
    6334586375119051935,
    6093398638321475389,
    6096083263464415963,
    6095713346521144919,
    6095988580910375034,
    6095706693616804285,
    6095657735284597191,
    6096183323317509438,
    6096183529475941311,
    6095949445168373144,
    6096035241435078733,
    6095675529334103687,
    6095785278633418890,
    6096043444822614389,
    6093522294724894291,
    6096167105521000703,
    6093861605731212875,
    6096054628917453455,
    6096115686172532857,
    6095961561271115744,
    6096148035866206608,
    6096132385005379427,
    6095865345413751303,
    6098136309371509564,
    6095724491961277782,
    6095893559053917535,
    6096022665770835861,
    6098201124722974324,
    6095825479527309554,
    6095803201531945360,
    6095903484723338612,
    6098260846243224336,
    6098069329356528539,
    6095659659429945869,
    6098091358243789738,
    6095830702207541814,
    6097888588542779911,
    6095902496880861629,
    6095650519739538680,
    6095675580873711995,
    6095673905836466207,
    6095664903585014100,
    6098155413386042411,
    6095740026857988145,
    6096064090730405777,
    6291780433239614475,
    6291978834958886683,
]

# Invisible-ish base: custom emoji entity replaces this; no normal star shown when premium works
_EMOJI_BASE = "\u200b"  # zero-width space fallback — Telegram needs a char; entity paints premium


def two_premium_emojis():
    """Return (prefix_text, formatting_entities) — 2 random premium custom emojis only."""
    ids = sample(CUSTOM_EMOJI_IDS, 2)
    # Use a single BMP emoji as base that gets fully replaced by custom emoji rendering
    base = "\U0001F3F7"  # 🏷 tag — length 2 in UTF-16
    # Prefer length-1 BMP for simpler offsets: use "\u2060" word joiner (invisible)
    base = "\u2060"
    text = base + base + " "
    entities = [
        MessageEntityCustomEmoji(offset=0, length=1, document_id=ids[0]),
        MessageEntityCustomEmoji(offset=1, length=1, document_id=ids[1]),
    ]
    return text, entities


async def send_with_premium_emojis(client, chat_id, body, reply_to=None):
    """Send text with 2 premium custom emojis prefix (no normal emoji)."""
    prefix, ents = two_premium_emojis()
    text = prefix + body
    kwargs = {"formatting_entities": ents}
    if reply_to is not None:
        kwargs["reply_to"] = reply_to
    await client.send_message(chat_id, text, **kwargs)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sraid(?: |$)(.*)" % hl))
async def raid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in ALTRON:
                await e.reply("ɪsɴᴇ ʜɪ ɪss ʙᴏᴛ ᴋᴏ ᴘʀᴏɢʀᴀᴍ ᴋɪʏᴀ ʜᴀɪ  sᴀᴍᴊʜᴀ ʟᴀᴜᴅᴜ😈")
            elif uid == OWNER_ID:
                await e.reply("ɪsɴᴇ ʜɪ ɪss ʙᴏᴛ ᴋᴏ ᴘʀᴏɢʀᴀᴍ ᴋɪʏᴀ ʜᴀɪ sᴀᴍᴊʜᴀ ʟᴀᴜᴅᴜ 😈")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(RAID)
                    body = f"{username} {reply}"
                    await send_with_premium_emojis(e.client, e.chat_id, body)
                    await asyncio.sleep(0.0)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐚𝐢𝐝\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True))
@X2.on(events.NewMessage(incoming=True))
@X3.on(events.NewMessage(incoming=True))
@X4.on(events.NewMessage(incoming=True))
@X5.on(events.NewMessage(incoming=True))
@X6.on(events.NewMessage(incoming=True))
@X7.on(events.NewMessage(incoming=True))
@X8.on(events.NewMessage(incoming=True))
@X9.on(events.NewMessage(incoming=True))
@X10.on(events.NewMessage(incoming=True))
async def _(event):
    global REPLY_RAID
    check = f"{event.sender_id}_{event.chat_id}"
    if check in REPLY_RAID:
        await asyncio.sleep(0.0)
        body = choice(REPLYRAID)
        await send_with_premium_emojis(
            event.client,
            event.chat_id,
            body,
            reply_to=event.message.id,
        )


@X1.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%srraid(?: |$)(.*)" % hl))
async def rraid(e):
    if e.sender_id in SUDO_USERS:
        mkrr = e.text.split(" ", 1)
        if len(mkrr) == 2:
            entity = await e.client.get_entity(mkrr[1])

        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            user_id = entity.id
            if user_id in ALTRON:
                await e.reply("ɪsɴᴇ ʜɪ ɪss ʙᴏᴛ ᴋᴏ ᴘʀᴏɢʀᴀᴍ ᴋᴇʏᴀ ʜᴀɪ sᴀᴍᴊʜᴀ ʟᴀᴜᴅᴜ😈")
            elif user_id == OWNER_ID:
                await e.reply("ɪsɴᴇ ʜɪ ɪss ʙᴏᴛ ᴋᴏ ᴘʀᴏɢʀᴀᴍ ᴋɪʏᴀ ʜᴀɪ sᴀᴍᴊʜᴀ ʟᴀᴜᴅᴜ😈 ")
            elif user_id in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                global REPLY_RAID
                check = f"{user_id}_{e.chat_id}"
                if check not in REPLY_RAID:
                    REPLY_RAID.append(check)
                await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ғᴜᴄᴋɪɴɢ sᴛᴀʀᴛ ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}rraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}rraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sdrraid(?: |$)(.*)" % hl))
async def drraid(e):
    if e.sender_id in SUDO_USERS:
        text = e.text.split(" ", 1)

        if len(text) == 2:
            entity = await e.client.get_entity(text[1])
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)

        try:
            check = f"{entity.id}_{e.chat_id}"
            global REPLY_RAID
            if check in REPLY_RAID:
                REPLY_RAID.remove(check)
            await e.reply("» ʀᴇᴘʟʏ ʀᴀɪᴅ ғᴜᴄᴋɪɴɢ sᴛᴏᴘ ✅")
        except NameError:
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐃𝐑𝐞𝐩𝐥𝐲𝐑𝐚𝐢𝐝\n  » {hl}drraid <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}drraid <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%smraid(?: |$)(.*)" % hl))
async def mraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(MRAID)
                body = f"{username} {reply}"
                await send_with_premium_emojis(e.client, e.chat_id, body)
                await asyncio.sleep(0.0)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗠𝗥𝗮𝗶𝗱\n  » {hl}mraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}mraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssraid(?: |$)(.*)" % hl))
async def sraid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            first_name = entity.first_name
            counter = int(xraid[1])
            username = f"[{first_name}](tg://user?id={uid})"
            for _ in range(counter):
                reply = choice(SRAID)
                body = f"{username} {reply}"
                await send_with_premium_emojis(e.client, e.chat_id, body)
                await asyncio.sleep(0.0)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝗦𝗥𝗮𝗶𝗱\n  » {hl}sraid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}sraid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%scraid(?: |$)(.*)" % hl))
async def craid(e):
    if e.sender_id in SUDO_USERS:
        xraid = e.text.split(" ", 2)

        if len(xraid) == 3:
            entity = await e.client.get_entity(xraid[2])
            uid = entity.id

        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id

        try:
            if uid in ALTRON:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀʟᴛʀᴏɴ'ꜱ ᴏᴡɴᴇʀ.")
            elif uid == OWNER_ID:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴏᴡɴᴇʀ ᴏꜰ ᴛʜᴇꜱᴇ ʙᴏᴛꜱ.")
            elif uid in SUDO_USERS:
                await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ꜱᴜᴅᴏ ᴜꜱᴇʀ.")
            else:
                first_name = entity.first_name
                counter = int(xraid[1])
                username = f"[{first_name}](tg://user?id={uid})"
                for _ in range(counter):
                    reply = choice(CRAID)
                    body = f"{username} {reply}"
                    await send_with_premium_emojis(e.client, e.chat_id, body)
                    await asyncio.sleep(0.0)
        except (IndexError, ValueError, NameError):
            await e.reply(f"𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲: 𝐂𝗥𝗮𝗶𝗱\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ᴜꜱᴇʀɴᴀᴍᴇ ᴏꜰ ᴜꜱᴇʀ>\n  » {hl}raid <ᴄᴏᴜɴᴛ> <ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)
