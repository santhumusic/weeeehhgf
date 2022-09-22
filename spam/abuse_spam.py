#telugu coders

import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import ABUSE_SPAM
from typing import Tuple
import random
import asyncio
from traceback import format_exc
from pyrogram.errors import FloodWait

@Client.on_message(filters.command(["spam"], [".", "!", "/"]))
async def spam(client: Client, message: Message):   
    await message.delete() 
    spam = await message.reply_text("**processing your spam....**")
    await message.delete() 
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    for _ in range(quantity):
        try: 
            text = random.choice(ABUSE_SPAM) 
            await client.send_message(chat_id=message.chat.id, message=text)       
        except FloodWait as e:
            await asyncio.sleep(e.x)
