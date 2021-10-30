from pyrez import SmiteAPI
from dotenv import load_dotenv
import os

load_dotenv()

DEVID = os.getenv("DEVID")
AUTHKEY = os.getenv("AUTHKEY")
print(AUTHKEY)

smite = SmiteAPI(DEVID, AUTHKEY)

print(smite.getDataUsed())
