from pyrogram import Client, filters
from spam.decorators import sudo_users_only
from pyrogram.types import Message

@Client.on_message(filters.command(["addsudo"], [".", "/", "!"]))
@sudo_users_only
async def banall(client: Client, message: Message):
    await message.edit("adding sudo....")
    await message.send_message("sudo added successfully") 

