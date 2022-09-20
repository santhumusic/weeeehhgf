import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("banall", ["."]))
async def banall(client: Client, message: Message):
    await message.delete()
    chat_id = message.chat.id
    icm = client.get_chat_members(chat_id)
    async for member in icm:
        string = f"/ban {member.user.mention}\n"
        await client.send_message(chat_id, text=string)
