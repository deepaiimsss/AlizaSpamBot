from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from telethon import events

a = False

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/spam'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/spam'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/spam'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/spam'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/spam'))
async def spam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[6:8])
            spam = text[8:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                    await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/bigspam'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/bigspam'))
async def bigspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[9:15])
            spam = text[15:]
            message = str(spam)
            if e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.message
                for i in range(counts):
                    await e.client.send_message(e.chat_id, replied_message)
            else:
                for i in range(counts):
                            await e.client.send_message(e.chat_id, message)
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Something went wrong!")

@AlizaBot1.on(events.NewMessage(incoming=True, pattern='/mspam'))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern='/mspam'))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern='/mspam'))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern='/mspam'))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern='/mspam'))
async def mspam(e):
    if e.sender_id in MY_USERS:
        try:
            text = e.raw_text
            counts = int(text[7:13])
            if e.is_reply == False:
                await e.client.send_message(e.chat_id, "Please reply to a media and enter how many times you want send that media!")
            elif e.is_reply == True:
                replied = await e.get_reply_message()
                replied_message = replied.media
                for i in range(counts):
                    await e.client.send_file(e.chat_id, replied_message)
            else:
                await e.client.send_message(e.chat_id, "Some thing went wrong! Please reply to a media and enter how many times you want send that media!")
        except Exception as er:
            print(er)
            await e.client.send_message(e.chat_id, "Please enter how many times you want to spam in reply of media!")

@AlizaBot1.on(events.NewMessage(incoming=True, pattern="/uspam"))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern="/uspam"))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern="/uspam"))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern="/uspam"))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspam(e):
    if e.sender_id in MY_USERS:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        
@AlizaBot1.on(events.NewMessage(incoming=True, pattern="/ustop"))
@AlizaBot2.on(events.NewMessage(incoming=True, pattern="/ustop"))
@AlizaBot3.on(events.NewMessage(incoming=True, pattern="/ustop"))
@AlizaBot4.on(events.NewMessage(incoming=True, pattern="/ustop"))
@AlizaBot5.on(events.NewMessage(incoming=True, pattern="/ustop"))
async def ustop(e):
    if e.sender_id in MY_USERS:
        global a
        a = False
        await e.client.send_message(e.chat_id, "U Spam Stopped Successfully")
