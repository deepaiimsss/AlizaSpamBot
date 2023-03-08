from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
Aliza Spam Bot Is Alive!
My Master:- {master}
Bot Version:- `{BOT_VERSION}`
Telethon Version:- `{version.__version__}`
{BIO_MSG}
"""

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/alive'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/alive'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/alive'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/alive'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)
