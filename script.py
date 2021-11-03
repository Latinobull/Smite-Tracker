from pyrez import SmiteAPI
from dotenv import load_dotenv
import os

import pyrez
from pyrez.api.StatusPageAPI import StatusPageAPI
from requests.models import to_native_string

load_dotenv()

DEVID = os.getenv("DEVID")
AUTHKEY = os.getenv("AUTHKEY")


smite = SmiteAPI(DEVID, AUTHKEY)
smiteStatus = StatusPageAPI()

# Player functions
msg = "An error has occured"


def getPlayer(name):
    while True:
        try:
            name = smite.getPlayer(name)
        except pyrez.exceptions.PlayerNotFound:
            print("Player does not exist or profile is hidden")
            break

        print(name.activePlayerId)
        getGodStats(name.activePlayerId,  'Aresreg')
        break


def getGodStats(userId, userGod):
    godStats = smite.getGodRanks(userId)

    for key in godStats:
        global thisGod
        if key.god == userGod:
            thisGod = key
        else:
            thisGod = msg
        print(thisGod)
# Status and Server Functions


def patchVersion():
    patch = smite.getPatchInfo()
    print(patch.version_string)


def serverStatus():
    server = smite.getServerStatus()
    for data in server:
        if data.status:
            status = "Servers are up"
        else:
            status = "Servers are down"
        print(data.platform, status)


def SmiteOperation():
    sOp = smiteStatus.getStatus()
    print(sOp.status.description)


def ScheduledMain():
    sMain = smiteStatus.getScheduledMaintenances(upcomingOnly=True)
    if sMain.scheduledMaintenances == []:
        msg = "There is no scheduled Maintenance"
    else:
        msg = sMain.scheduledMaintenances
    print(msg)


def Incidents():
    incidents = smiteStatus.getIncidents(unresolvedOnly=True)
    if incidents.incidents == []:
        msg = 'There are no incidents'
    else:
        msg = incidents.incidents
    print(msg)


Incidents()
getPlayer('Rexsi')
