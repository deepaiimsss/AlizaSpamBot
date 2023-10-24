from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from telethon import events, Button


data  = [
    Button.url("Creator", url="t.me/sakku_cute"),
    Button.url("Channel", url="t.me/Aliza_update"),
    Button.url("Group", url="t.me/Aliza_support")
]


@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[ ‌‌‌‌≛⃝👑≛⃝ʂαƙƙυ ≛⃝ 👑≛⃝](tg://user?id={1407312928})"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
Hey {mention},
This Is Aliza Spam Bot!
Owner:- {myOwner}
Sudo:- {sudo_user}
Creator:- {creator}
    """
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
