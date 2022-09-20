import asyncio
import random
import time
from pyrogram.types import Message
from config import SUDO_USERS as sudo_user
from config import PORN
from main import API_ID, API_HASH, STRING_SESSION 
from traceback import format_exc
from typing import Tuple
from pyrogram import Client, filters


user = Client(
    STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
)


@Client.on_message(filters.user(sudo_user) & filters.command(["porn"], [".", "!", "/"]))
async def porn(client: Client, msg: Message):       
    await msg.edit(random.choice(PORNS))


user.run() 
