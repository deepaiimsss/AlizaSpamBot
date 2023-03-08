import sys
import glob
from pathlib import Path
from sys import argv
from spambot import *
from spambot import AlizaBot1, AlizaBot2, AlizaBot3, AlizaBot4, AlizaBot5
from spambot.utils import load_plugs

if __name__ == "__main__":
    modules = "spambot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

import spambot
import spambot.userNeeds
import spambot.help
import spambot.helpers.callbackQuery

print("\n\n⚡Aliza Spam Bot Deployed Successfully⚡\n\n")

if len(argv) not in (1, 3, 4):
    try:
        AlizaBot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot5.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        AlizaBot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        AlizaBot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
