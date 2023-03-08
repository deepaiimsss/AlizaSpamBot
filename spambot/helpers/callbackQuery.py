from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from spambot.help import *
from spambot.helpers.commands import *
from telethon import events


@AlizaBot1.on(events.CallbackQuery(data=b'alive'))
@AlizaBot2.on(events.CallbackQuery(data=b'alive'))
@AlizaBot3.on(events.CallbackQuery(data=b'alive'))
@AlizaBot4.on(events.CallbackQuery(data=b'alive'))
@AlizaBot5.on(events.CallbackQuery(data=b'alive'))
async def alive_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'ping'))
@AlizaBot2.on(events.CallbackQuery(data=b'ping'))
@AlizaBot3.on(events.CallbackQuery(data=b'ping'))
@AlizaBot4.on(events.CallbackQuery(data=b'ping'))
@AlizaBot5.on(events.CallbackQuery(data=b'ping'))
async def ping_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'raid'))
@AlizaBot2.on(events.CallbackQuery(data=b'raid'))
@AlizaBot3.on(events.CallbackQuery(data=b'raid'))
@AlizaBot4.on(events.CallbackQuery(data=b'raid'))
@AlizaBot5.on(events.CallbackQuery(data=b'raid'))
async def raid_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'replyraid'))
@AlizaBot2.on(events.CallbackQuery(data=b'replyraid'))
@AlizaBot3.on(events.CallbackQuery(data=b'replyraid'))
@AlizaBot4.on(events.CallbackQuery(data=b'replyraid'))
@AlizaBot5.on(events.CallbackQuery(data=b'replyraid'))
async def replyraid_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'spam'))
@AlizaBot2.on(events.CallbackQuery(data=b'spam'))
@AlizaBot3.on(events.CallbackQuery(data=b'spam'))
@AlizaBot4.on(events.CallbackQuery(data=b'spam'))
@AlizaBot5.on(events.CallbackQuery(data=b'spam'))
async def spam_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'pspam'))
@AlizaBot2.on(events.CallbackQuery(data=b'pspam'))
@AlizaBot3.on(events.CallbackQuery(data=b'pspam'))
@AlizaBot4.on(events.CallbackQuery(data=b'pspam'))
@AlizaBot5.on(events.CallbackQuery(data=b'pspam'))
async def pspam_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'extras'))
@AlizaBot2.on(events.CallbackQuery(data=b'extras'))
@AlizaBot3.on(events.CallbackQuery(data=b'extras'))
@AlizaBot4.on(events.CallbackQuery(data=b'extras'))
@AlizaBot5.on(events.CallbackQuery(data=b'extras'))
async def extras_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'heroku'))
@AlizaBot2.on(events.CallbackQuery(data=b'heroku'))
@AlizaBot3.on(events.CallbackQuery(data=b'heroku'))
@AlizaBot4.on(events.CallbackQuery(data=b'heroku'))
@AlizaBot5.on(events.CallbackQuery(data=b'heroku'))
async def heroku(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit(f"{HEROKU_CMD}", buttons=BACK)

@AlizaBot1.on(events.CallbackQuery(data=b'back'))
@AlizaBot2.on(events.CallbackQuery(data=b'back'))
@AlizaBot3.on(events.CallbackQuery(data=b'back'))
@AlizaBot4.on(events.CallbackQuery(data=b'back'))
@AlizaBot5.on(events.CallbackQuery(data=b'back'))
async def back_query(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("Only Owner, Co-Owner And Sudo Users Can Access This Buttons!", cache_time=0, alert=True)
    else:
        await e.edit("This Is Help Command!!!", buttons=Buttons)
 
