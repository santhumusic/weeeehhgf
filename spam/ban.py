from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message
from spam import bot
from pyrogram.types import *
from config import SUDO_USERS


@Client.on_message(filters.command(["banall"], [".", "/", "!"])) 
async def banall(client: Client, message: Message):
    await message.reply_text(" Banning all members😑") 
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.kick_chat_member(chat_id =message.chat.id,user_id=alls.user.id)
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass
