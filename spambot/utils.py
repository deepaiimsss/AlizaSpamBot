import sys
import logging
import importlib
from pathlib import Path


def load_plugs(plugname):
    modules = Path(f"spambot/plugins/{plugname}.py")
    myfiles = f"spambot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["spambot.plugins." + plugname] = load
    print("AlizaSpamBot - Successfully Imported " + plugname)
