from pyrogram import Client, filters
from spam.decorators import sudo_users_only

@Sclient.on_message(filters.command(["addsudo"], [".", "/", "!"]))
@sudo_users_only
async def banall(client: Client, message: Message):

