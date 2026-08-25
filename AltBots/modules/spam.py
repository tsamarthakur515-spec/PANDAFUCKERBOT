# © @ALONE_WAS_BOT
import asyncio
from random import choice, sample

from AltBots.data import GROUP, PORMS
from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl

from telethon import events, functions, types
from telethon.tl.types import MessageEntityCustomEmoji

# Same premium custom emoji IDs as raid
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
    ids = sample(CUSTOM_EMOJI_IDS, 2)
    base = "\u2060"  # invisible word joiner — only premium shows when entity works
    text = base + base + " "
    entities = [
        MessageEntityCustomEmoji(offset=0, length=1, document_id=ids[0]),
        MessageEntityCustomEmoji(offset=1, length=1, document_id=ids[1]),
    ]
    return text, entities


async def send_spam_text(client, chat_id, message, reply_to=None):
    prefix, ents = two_premium_emojis()
    text = prefix + message
    kwargs = {"formatting_entities": ents}
    if reply_to is not None:
        kwargs["reply_to"] = reply_to
    await client.send_message(chat_id, text, **kwargs)


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=smex.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(event: events):
    if event.sender_id in SUDO_USERS:
        altron = event.text.split(" ", 2)
        mk = await event.get_reply_message()

        try:
            if len(altron) == 3:
                message = altron[2]
                for _ in range(int(altron[1])):
                    if event.reply_to_msg_id:
                        await send_spam_text(
                            event.client,
                            event.chat_id,
                            message,
                            reply_to=event.reply_to_msg_id,
                        )
                    else:
                        await send_spam_text(event.client, event.chat_id, message)
                    await asyncio.sleep(0.0)
            elif event.reply_to_msg_id and mk.media:
                for _ in range(int(altron[1])):
                    mk = await event.client.send_file(event.chat_id, mk, caption=mk.text)
                    await gifspam(event, mk)
                    await asyncio.sleep(0.0)
            elif event.reply_to_msg_id and mk.text:
                message = mk.text
                for _ in range(int(altron[1])):
                    await send_spam_text(event.client, event.chat_id, message)
                    await asyncio.sleep(0.0)
            else:
                await event.reply(f"😈 **Usage:**\n  » {hl}spam 13 Altron\n  » {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » {hl}spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")

        except (IndexError, ValueError):
            await event.reply(f"😈 **Usage:**\n  » {hl}spam 13 Altron\n  » {hl}spam 13 <ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ>\n\n**To do spam with replying to a user:**\n  » {hl}spam 13 Altron <ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ>")
        except Exception as e:
            print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%spspam(?: |$)(.*)" % hl))
async def pspam(event):
    if event.sender_id in SUDO_USERS:
        if event.chat_id in GROUP:
            await event.reply("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        else:
            try:
                counter = int(event.text.split(" ", 2)[1])
                porrn = choice(PORMS)
                for _ in range(counter):
                    alt = await event.client.send_file(event.chat_id, porrn)
                    await gifspam(event, alt)
                    await asyncio.sleep(0.0)
            except (IndexError, ValueError):
                await event.reply(f"🔞 **Usage:**  {hl}pspam 13")
            except Exception as e:
                print(e)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shang(?: |$)(.*)" % hl))
async def hang(e):
    if e.sender_id in SUDO_USERS:
        if e.chat_id in GROUP:
            await e.reply("» ꜱᴏʀʀʏ, ᴛʜɪꜱ ɪꜱ ᴀʟᴛʀᴏɴ ᴘʀᴏᴛᴇᴄᴛᴇᴅ ɢʀᴏᴜᴘ.")
        else:
            try:
                counter = int(e.text.split(" ", 2)[1])
                hang = "😈" * 500
                for _ in range(counter):
                    await e.respond(hang)
                    await asyncio.sleep(0.0)
            except (IndexError, ValueError):
                await e.reply(f"😈 **Usage:** {hl}hang 10")
            except Exception as e:
                print(e)
