from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message
from spam import bot
from pyrogram.types import *
from config import SUDO_USERS


@Client.on_message(filters.command(["banall"], [".", "/", "!"])) 
async def banall(client: Client, message: Message):
    await client.ban_chat_member(message.chat.id, user.id, 0)
