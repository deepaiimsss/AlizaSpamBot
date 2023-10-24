import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "3933412"))
    API_HASH = os.environ.get("API_HASH", "97364437b0bf42e25745e25f1c536189")
    BOT_TOKEN1 = os.environ.get("BOT_TOKEN1", "5457915605:AAHw3Oo3gIB-rELXL-VQiRyY-u00CHAmgEI")
    BOT_TOKEN2 = os.environ.get("BOT_TOKEN2", "5748926642:AAE6knIAlbBaSst9wD7FnanOlyUZBIJlRB8")
    BOT_TOKEN3 = os.environ.get("BOT_TOKEN3", "5529110275:AAEJPsspJmI5fYNl2fvQgFkxxEIhKRHP_HI")
    BOT_TOKEN4 = os.environ.get("BOT_TOKEN4", "5717105219:AAExAPCdl10DLsUyruuMwh1XrctRqeI8DW4")
    BOT_TOKEN5 = os.environ.get("BOT_TOKEN5", "5545960274:AAHtHGP_cOwiKy1D0bGL3RCisdrxPvHH7JE")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5386820700"))
    OWNER_NAME = os.environ.get("OWNER_NAME", "Deep")
    OWNER_USERNAME =os.environ.get("OWNER_USERNAME", "Itz_me_AR")
    DISPLAY_PIC = os.environ.get("DISPLAY_PIC", "https://graph.org/file/99eb35e73777775a57528.jpg")
    BIO_MSG =  os.environ.get("BIO_MSG", "Maa Chudao Shavvu and Shekhu")
