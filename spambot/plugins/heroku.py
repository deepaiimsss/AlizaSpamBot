import heroku3
from spambot import *
from telethon import events
from spambot.helpers.neko import paster


@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/restart'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/restart'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/restart'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/restart'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/restart'))
async def restart(e):
    if e.sender_id in MY_USERS:
        if (HEROKU_API_KEY is not None) or (HEROKU_APP_NAME is not None):
            try:
                await e.client.send_message(e.chat_id, "`Restarting...`")
                heroku_conn = heroku3.from_key(HEROKU_API_KEY)
                app = heroku_conn.app(HEROKU_APP_NAME)
                app.restart()
            except Exception as er:
                print(er)
        else:
            await e.client.send_message(e.chat_id, "Please Put `HEROKU_APP_NAME` And `HEROKU_API_KEY` In Heroku Vars!")

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/logs'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/logs'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/logs'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/logs'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/logs'))
async def restart(e):
    if e.sender_id in MY_USERS:
        if (HEROKU_API_KEY is not None) or (HEROKU_APP_NAME is not None):
            try:
                heroku_conn = heroku3.from_key(HEROKU_API_KEY)
                app = heroku_conn.app(HEROKU_APP_NAME)
                log = app.get_log()
                logs1 = await paster(log)
                paste = f"[Click Here To Check Logs]({logs1})"
                await e.client.send_message(e.chat_id, f"Aliza Spam Userbot Logs:- {paste}\n")  
            except Exception as er:
                print(er)
        else:
            await e.client.send_message(e.chat_id, "Please Put `HEROKU_APP_NAME` And `HEROKU_API_KEY` In Heroku Vars!")
