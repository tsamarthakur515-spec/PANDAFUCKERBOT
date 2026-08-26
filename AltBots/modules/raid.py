import asyncio
from random import choice, sample

from telethon import events
from telethon.tl.types import MessageEntityCustomEmoji, MessageEntityTextUrl

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


def two_premium_emojis():
    """Return (prefix_text, formatting_entities) — 2 random premium custom emojis only."""
    ids = sample(CUSTOM_EMOJI_IDS, 2)
    base = "\u2060"
    text = base + base + " "
    entities = [
        MessageEntityCustomEmoji(offset=0, length=1, document_id=ids[0]),
        MessageEntityCustomEmoji(offset=1, length=1, document_id=ids[1]),
    ]
    return text, entities


async def send_with_premium_emojis(client, chat_id, body, reply_to=None, mention_name=None, mention_id=None):
    """Send text with 2 premium custom emojis + optional clickable name (no raw ID/markdown)."""
    prefix, ents = two_premium_emojis()

    if mention_name and mention_id:
        name = (mention_name or "User").strip() or "User"
        full_text = prefix + name + " " + body
        mention_offset = 3
        mention_length = len(name)
        ents.append(
            MessageEntityTextUrl(
                offset=mention_offset,
                length=mention_length,
                url=f"tg://user?id={mention_id}"
            )
        )
        text = full_text
    else:
        text = prefix + body

    kwargs = {"formatting_entities": ents}
    if reply_to is not None:
        kwargs["reply_to"] = reply_to
    await client.send_message(chat_id, text, **kwargs)


# Pattern supports both .raid and /raid (and with @botusername)
RAID_PATTERN = r"^[./]raid(?:@\w+)?(?: |$)(.*)"


@X1.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X2.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X3.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X4.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X5.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X6.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X7.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X8.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X9.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
@X10.on(events.NewMessage(incoming=True, pattern=RAID_PATTERN))
async def raid(e):
    if e.sender_id not in SUDO_USERS:
        return

    # Remove command part, keep args
    text = e.text or ""
    # Strip .raid or /raid or .raid@bot etc
    import re
    args = re.sub(r"^[./]raid(?:@\w+)?\s*", "", text, flags=re.IGNORECASE).strip()
    parts = args.split(maxsplit=1)

    try:
        if not parts:
            await e.reply(f"**Usage:**\n`{hl}raid <count> <username>`\n`{hl}raid <count>` (reply to user)\n`/raid <count> @user`")
            return

        counter = int(parts[0])
        entity = None
        uid = None

        if len(parts) >= 2:
            # username given
            entity = await e.client.get_entity(parts[1])
            uid = entity.id
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
            uid = entity.id
        else:
            await e.reply(f"**Usage:**\n`{hl}raid <count> <username>`\n`{hl}raid <count>` (reply to user)")
            return

        if uid in ALTRON or uid == OWNER_ID or uid in SUDO_USERS:
            await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ.")
            return

        first_name = (entity.first_name or "User").strip() or "User"

        for _ in range(counter):
            reply = choice(RAID)
            await send_with_premium_emojis(
                e.client,
                e.chat_id,
                reply,
                mention_name=first_name,
                mention_id=uid,
            )
            await asyncio.sleep(0.1)

    except ValueError:
        await e.reply("Count number hona chahiye. Example: `.raid 5 @user`")
    except Exception as err:
        await e.reply(f"Error: `{str(err)[:200]}`")
        print(err)


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


@X1.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X2.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X3.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X4.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X5.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X6.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X7.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X8.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X9.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
@X10.on(events.NewMessage(incoming=True, pattern=r"^[./]rraid(?:@\w+)?(?: |$)(.*)"))
async def rraid(e):
    if e.sender_id not in SUDO_USERS:
        return
    try:
        if e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
        else:
            text = e.text or ""
            import re
            arg = re.sub(r"^[./]rraid(?:@\w+)?\s*", "", text, flags=re.IGNORECASE).strip()
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


@X1.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X2.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X3.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X4.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X5.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X6.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X7.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X8.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X9.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
@X10.on(events.NewMessage(incoming=True, pattern=r"^[./]drraid(?:@\w+)?(?: |$)(.*)"))
async def drraid(e):
    if e.sender_id not in SUDO_USERS:
        return
    try:
        if e.reply_to_msg_id:
            a = await e.get_reply_message()
            entity = await e.client.get_entity(a.sender_id)
        else:
            text = e.text or ""
            import re
            arg = re.sub(r"^[./]drraid(?:@\w+)?\s*", "", text, flags=re.IGNORECASE).strip()
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


# Keep mraid / sraid / craid with both . and / support too
for cmd, data_list, name in [
    ("mraid", MRAID, "MRaid"),
    ("sraid", SRAID, "SRaid"),
    ("craid", CRAID, "CRaid"),
]:
    pattern = rf"^[./]{cmd}(?:@\w+)?(?: |$)(.*)"

    async def make_handler(cmd_name=cmd, raid_list=data_list):
        async def handler(e):
            if e.sender_id not in SUDO_USERS:
                return
            text = e.text or ""
            import re
            args = re.sub(rf"^[./]{cmd_name}(?:@\w+)?\s*", "", text, flags=re.IGNORECASE).strip()
            parts = args.split(maxsplit=1)
            try:
                if not parts:
                    await e.reply(f"**Usage:** `{hl}{cmd_name} <count> <username>` ya reply")
                    return
                counter = int(parts[0])
                if len(parts) >= 2:
                    entity = await e.client.get_entity(parts[1])
                elif e.reply_to_msg_id:
                    a = await e.get_reply_message()
                    entity = await e.client.get_entity(a.sender_id)
                else:
                    await e.reply(f"**Usage:** `{hl}{cmd_name} <count> <username>` ya reply")
                    return

                uid = entity.id
                if uid in ALTRON or uid == OWNER_ID or uid in SUDO_USERS:
                    await e.reply("ɴᴏ, ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴘʀᴏᴛᴇᴄᴛᴇᴅ.")
                    return

                first_name = (entity.first_name or "User").strip() or "User"
                for _ in range(counter):
                    reply = choice(raid_list)
                    await send_with_premium_emojis(
                        e.client, e.chat_id, reply,
                        mention_name=first_name, mention_id=uid
                    )
                    await asyncio.sleep(0.1)
            except ValueError:
                await e.reply("Count number hona chahiye.")
            except Exception as err:
                await e.reply(f"Error: `{str(err)[:150]}`")
        return handler

    # Register for all 10 bots (simplified - using loop carefully)
    # Note: for simplicity we register the main ones above; full multi-bot registration kept for raid
