import asyncio
import random
import time
from pyrogram.types import Message
from config import SUDO_USER as sudo_user
from config import PROGROUPS, PORNS
from traceback import format_exc
from typing import Tuple




@Client.on_message(filters.user(sudo_user) & filters.command(["porn"], [".", "!", "/"]))
async def prd(client: Client, message: Message):       
    sex = await message.reply_text("`Processing..`")
    quantity = message.command[1]
    failed = 0 
    quantity = int(quantity)
    if int(message.chat.id) in PROGROUPS:
        await sex.edit("`Baap Ke Group Me Spam Nahi!`")
        return    
    for _ in range(quantity):
        try: 
            file = random.choice(PORN) 
            await client.send_video(chat_id=message.chat.id, video=file)       
