import random
from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from spambot.helpers.plinks import PLINKS
from telethon import events

a = False

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/pspam'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/pspam'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/pspam'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/pspam'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/pspam'))
async def pspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        elif e.raw_text[6:] == "":
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    p = random.choice(PLINKS)
                    await e.client.send_file(e.chat_id, p, caption=message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to pspam!")
        
@AlizaBot1.on(events.NewMessage(incoming=True, pattern="/pstop"))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern="/pstop"))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern="/pstop"))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern="/pstop"))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern="/pstop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "Porn Spam Stopped Successfully")
