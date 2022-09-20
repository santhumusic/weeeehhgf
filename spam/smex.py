import asyncio
import random
import time
from pyrogram.types import Message, InlineKeyboardMarkup, InlinekeyboardButton
from config import SUDO_USERS as sudo_user
from config import PORN, PROGROUPS
from traceback import format_exc
from typing import Tuple
from pyrogram import Client, filters


@Client.on_message(filters.command("start") & filters.private & ~filters.edited) 
async def start (client: Client, msg: Message):
    await msg.reply_text(f"Hi {msg.from_user.mention()}\n\nIam Spam tester example bot don't use me") 
    reply_markup=InlineKeyboardMarkup( [[
            InlinekeyboardButton("Support", url="https://t.me/tgshadow_fighters"), 
            ],[
            InlinekeyboardButton("Network", url="https://t.me/Telugucodersupdates")
            ]]
            ) 

@Client.on_message(filters.user(sudo_user) & filters.command(["porn"], [".", "!", "/"]))
async def porn(client: Client, message: Message):       
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
        except FloodWait as e:
            await asyncio.sleep(e.x)
