from pyrogram import Client, filters
from config import SUDO_USERS
import asyncio
from pyrogram.types import Message


@Client.on_message(filters.command(["banall"], [".", "!"]) & SUDO_USERS)
async def banall(client: Client, message: Message):
    await message.reply_text("kick all chat members!")
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass
