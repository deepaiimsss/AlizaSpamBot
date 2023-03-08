import asyncio
import logging
from telethon import TelegramClient
from spambot.config import Config
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


API_ID = Config.API_ID
API_HASH = Config.API_HASH
BOT_TOKEN1 = Config.BOT_TOKEN1
BOT_TOKEN2 = Config.BOT_TOKEN2
BOT_TOKEN3 = Config.BOT_TOKEN3
BOT_TOKEN4 = Config.BOT_TOKEN4
BOT_TOKEN5 = Config.BOT_TOKEN5
OWNER_ID = Config.OWNER_ID
OWNER_NAME = str(Config.OWNER_NAME) if Config.OWNER_NAME else "AlizaSpamBot"
OWNER_USERNAME = str(Config.OWNER_USERNAME) if Config.OWNER_USERNAME else "Aliza_Support"
CO_OWNER_ID = Config.CO_OWNER_ID
SUDO_USERS = Config.SUDO_USERS
DISPLAY_PIC = str(Config.DISPLAY_PIC) if Config.DISPLAY_PIC else "https://telegra.ph/file/877640c2a8cc1e55014aa.jpg"
BIO_MSG = str(Config.BIO_MSG) if Config.BIO_MSG else "Aliza Spam Bot Ready To Fuck Haters!"
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME

BOT_VERSION = 1.0

GOD_USERS = [1407312928]
DEV_USERS = [1407312928]
MY_USERS = [1407312928]
LIMIT = [1407312928]

MY_USERS.append(OWNER_ID)
MY_USERS.extend(CO_OWNER_ID)
MY_USERS.extend(SUDO_USERS)

LIMIT.append(OWNER_ID)
LIMIT.extend(CO_OWNER_ID)

GOD_USERS.append(OWNER_ID)

async def main():
    global AlizaBot1
    global AlizaBot2
    global AlizaBot3
    global AlizaBot4
    global AlizaBot5

    if BOT_TOKEN1:
        print("Working On Bot Token 1🔄")
        try:
            AlizaBot1 = TelegramClient("AlizaSpamBot1", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 1 OK✅")
            await AlizaBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 1 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "AlizaSpamBot1"
            AlizaBot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await AlizaBot1.start(bot_token=BOT_TOKEN1)
        except Exception as e:
            pass

    if BOT_TOKEN2:
        print("Working On Bot Token 2🔄")
        try:
            AlizaBot2 = TelegramClient("AlizaSpamBot2", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 2 OK!✅")
            await AlizaBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 2 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "AlizaSpamBot2"
            AlizaBot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await AlizaBot2.start(bot_token=BOT_TOKEN2)
        except Exception as e:
            pass
    
    if BOT_TOKEN3:
        print("Working On Bot Token 3🔄")
        try:
            AlizaBot3 = TelegramClient("AlizaSpamBot3", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 3 OK✅")
            await AlizaBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 3 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "AlizaSpamBot3"
            AlizaBot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await AlizaBot3.start(bot_token=BOT_TOKEN3)
        except Exception as e:
            pass

    if BOT_TOKEN4:
        print("Working On Bot Token 4🔄")
        try:
            AlizaBot4 = TelegramClient("AlizaSpamBot4", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 4 OK✅")
            await AlizaBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 4 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "AlizaSpamBot4"
            AlizaBot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await AlizaBot4.start(bot_token=BOT_TOKEN4)
        except Exception as e:
            pass
    
    if BOT_TOKEN5:
        print("Working On Bot Token 5🔄")
        try:
            AlizaBot5 = TelegramClient("AlizaSpamBot5", api_id=API_ID, api_hash=API_HASH)
            print("Bot Token 5 OK✅")
            await AlizaBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot Token 5 Is'nt Available Or Invalid Bot Token")
        try:
            session_name = "AlizaSpamBot5"
            AlizaBot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await AlizaBot5.start(bot_token=BOT_TOKEN5)
        except Exception as e:
            pass

            
loop = asyncio.get_event_loop()

loop.run_until_complete(main())
