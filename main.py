import logging
from pyrogram import Client, filters
from pyrogram.types import *
import requests
import os
import re
import asyncio
from datetime import datetime
from config import *
from typing import Tuple

from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

API_ID = API_ID
API_HASH = API_HASH 
SUDO_USERS = SUDO_USERS
BOT_TOKEN = BOT_TOKEN

if not BOT_TOKEN:
    logging.error("Authorized bot token error")
    quit(1)

if not API_ID:
    logging.error("No Api-ID Found! Exiting!")
    quit(1)

if not API_HASH:
    logging.error("No ApiHash Found! Exiting!")
    quit(1) 

bot = Bot(
    ":spambot:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="spam")
)

bot.run
