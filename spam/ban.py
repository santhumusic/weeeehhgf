from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message


@Client.on_message(filters.command(["kickall", "banall"], [".", "!"]))
@Client.on_message(filters.command('kickall', ["."]))
async def kickall(client: Client, message: Message):
    member = client.get_chat_members(message.chat.id)
    async for alls in member:
        try:
            await client.ban_chat_member(message.chat.id, alls.user.id, 0)
        except:
            pass
