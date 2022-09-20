import asyncio
import random
import time
from pyrogram.types import Message
from config import SUDO_USERS 
from config import PORN
from traceback import format_exc
from typing import Tuple
from pyrogram import Client, filters


@Client.on_message(filters.command("start") & filters.private & ~filters.edited) 
async def start (client: Client, msg: Message):
    await msg.reply_text(f"Hi {msg.from_user.mention()}\n\nIam Spam tester example bot don't use me") 

@Client.on_message(filters.me & filters.command("porn") & SUDO_USERS)
async def porn(client: Client, msg: Message):       
    await msg.edit(random.choice(PORN))
