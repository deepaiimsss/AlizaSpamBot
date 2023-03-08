import os
from spambot import *
from spambot import AlizaBot1
from pathlib import Path
from telethon import events
from spambot.utils import load_plugs

@AlizaBot1.on(events.NewMessage(incoming=True, pattern="/install"))
async def install(e):
    if e.sender_id in MY_USERS:
        ok = await e.client.send_message(e.chat_id, "`Installing Given Module!`")
        if e.reply_to_msg_id:
            module = await e.get_reply_message()
            try:
                message = await e.client.download_media(module, "./spambot/plugins/")
                if "(" not in message:
                    mypath = Path(message)
                    name = mypath.stem
                    load_plugs(name.replace(".py", ""))
                    await e.client.edit_message(ok, f"`{name} Installed Successfully!`")
            except Exception as er:
                await e.client.edit_message(ok, f"`Can't Install {name}!`\n\nError:- {str(er)}")
                os.remove(message)

@AlizaBot1.on(events.NewMessage(incoming=True, pattern="/uninstall"))
async def uninstall(e):
    if e.sender_id in MY_USERS:
        text = e.raw_text[11:]
        mypath = f"./spambot/plugins/{text}.py"
        try:
            os.remove(mypath)
            await e.client.send_message(e.chat_id, f"`{text} Uninstalled Successfully!`")
        except Exception as er:
            await e.client.send_message(e.chat_id, f"`Can't Uninstall {text}!`\n\nError:- {str(er)}")
