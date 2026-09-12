    caption = TEXT.format(
        first_name=event.sender.first_name or "Friend",
        bot_name=bot_name,
        bot_id=bot_id,
        __version__=__version__
    )

    await event.client.send_file(
        event.chat_id,
        VIDEO_URL,
        caption=caption,
        buttons=START_BUTTON,
        parse_mode="html",
        supports_streaming=True
    )


async def button_handler(event):
    data = event.data.decode("utf-8")

    if data == "repo":
        await event.answer(
            "Bhag ja bheekhari, khud se bana le repo 😐\n\nPowered by sxyaru × Aru × Bots",
            alert=True
        )


# ==================== ATTACH TO ALL BOTS ====================
for bot in BOTS:
    bot.add_event_handler(button_handler, events.CallbackQuery)

for bot in BOTS:
    bot.add_event_handler(start_handler, events.NewMessage(pattern="/start"))
