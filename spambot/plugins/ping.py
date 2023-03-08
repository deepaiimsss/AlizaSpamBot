from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from telethon import events
from datetime import datetime

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/ping'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/ping'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/ping'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/ping'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/ping'))
async def ping(e):
    if e.sender_id in MY_USERS:
        before = datetime.now()
        message = await e.client.send_message(e.chat_id, "`Pinging.....!`")
        after = datetime.now()
        ms = (after - before).microseconds / 1000
        await e.client.edit_message(message, f"Ping Pong!\n\nAliza Spam Bot\n\nMy Master:- [{OWNER_NAME}](tg://user?id={OWNER_ID})\n\nPing:- {ms} ms\n\nAliza Spam Bot On Fire")
