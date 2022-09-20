import logging
from pyrogram import Client, filters
from pyrogram.types import *
import requests
import os
import re
import asyncio
import random
from datetime import datetime
from config import SUDO_USERS as sudo_user
from config import PORN
from config import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = API_ID
API_HASH = API_HASH 
SUDO_USERS = SUDO_USERS
STRING_SESSION = STRING_SESSION

if not STRING_SESSION:
    logging.error("No String Session Found! Exiting!")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1) 


user = Client(
    STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)


@Client.on_message(filters.command(["porn"], [".", "!", "/"]))
@sudo_user
async def porn(client: Client, msg: Message):       
    await msg.edit(random.choice(PORN))


user.run() 
