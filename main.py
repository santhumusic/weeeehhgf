import logging
from pyrogram import Client, filters, idle
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *
from pyrogram import Client as Bot

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


bot = Bot(
    ":telugucoders:",
    API_ID,
    API_HASH,
    string_session=STRING_SESSION,
) 


async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await bot.stop() 
    print("[INFO]: STOPPING BOT & USERBOT")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
