import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", None))
    API_HASH = os.environ.get("API_HASH", None)
    BOT_TOKEN1 = os.environ.get("BOT_TOKEN1", None)
    BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", None)
    BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", None)
    BOT_TOKEN4 = os.environ.get("BOT_TOKEN4", None)
    BOT_TOKEN5 = os.environ.get("BOT_TOKEN5", None)
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    OWNER_NAME = os.environ.get("OWNER_NAME", None)
    OWNER_USERNAME =os.environ.get("OWNER_USERNAME", None)
    CO_OWNER_ID = set(int(x) for x in os.environ.get("CO_OWNER_ID", None).split())
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", None).split())
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_ID", None)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    DISPLAY_PIC = os.environ.get("DISPLAY_PIC", None)
    BIO_MSG =  os.environ.get("BIO_MSG", None)
