import json
import requests
from spambot import *


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

async def paster(log):
    url = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": log}
    try:
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
    except Exception as er:
        print(str(er))

    if r.ok:
        r = r.json()
        logurl = f"https://pasty.lus.pm/{r['id']}.txt"
        return logurl
    return "`Pasty Temporary Not Available!`"
