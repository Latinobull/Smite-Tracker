import sys
from pyrez import SmiteAPI
from dotenv import load_dotenv
import os

import pyrez

load_dotenv()

DEVID = os.getenv("DEVID")
AUTHKEY = os.getenv("AUTHKEY")


smite = SmiteAPI(DEVID, AUTHKEY)


def getPlayer(name):
    while True:
        try:
            name = smite.getPlayer(name)
        except pyrez.exceptions.PlayerNotFound:
            print("Player does not exist or profile is hidden")
            break

        print(name.activePlayerId)
        print(name)
        break


getPlayer("jmvega316")
