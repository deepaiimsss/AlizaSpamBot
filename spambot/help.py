from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from spambot.helpers.commands import *
from telethon import events, Button


Buttons = [
    Button.inline("Alive", b'alive'),
    Button.inline("Ping", b'ping')
], [
    Button.inline("Raid", b'raid'),
    Button.inline("Reply Raid", b'replyraid')
], [
    Button.inline("Spam", b'spam'),
    Button.inline("Pspam", b'pspam')
], [
    Button.inline("Extras", b'extras'),
    Button.inline("Heroku", b'heroku')
], [
    Button.url("Creator", "t.me/sakku_cute"),
    Button.url("Channel", "t.me/Aliza_update"),
    Button.url("Group", "t.me/Aliza_support")
]

BACK = [
    Button.inline("Back", b'back')
]

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/help'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/help'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/help'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/help'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(e):
    if e.sender_id in MY_USERS:
        message = await e.client.send_file(e.chat_id, DISPLAY_PIC, caption="This Is Help Command!!!", buttons=Buttons)

        
