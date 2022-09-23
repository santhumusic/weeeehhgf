from pyrogram import Client, filters

@Sclient.on_message(filters.command(["addsudo"], [".", "/", "!"]))
@sudo_users_only
async def banall(client: Client, message: Message):

