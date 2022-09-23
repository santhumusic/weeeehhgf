from pyrogram import Client, filters
from spam.decorators import sudo_users_only
from pyrogram.types import Message
from spam.decorators import add_sudo, remove_sudo
from config import SUDO_USERS, OWNER_ID
from spam import bot

@bot.on_message(filters.command(["addsudo"], [".", "/", "!"])) 
async def useradd(client: Client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await bot.get_users(user)
        if user.id in SUDO_USERS:
            return await message.reply_text("{0} is already a sudo user.".format(user.mention))
        if user.id in SUDO_USERS:
            await message.reply_text("Added **{0}** to Sudo Users.".format(user.mention))
        return
    if user.id in SUDO_USERS:
        await message.reply_text("{0} is already a sudo user.".format(user.mention))
    if user.id in SUDO_USERS:
        await message.reply_text(
            "Added **{0}** to Sudo Users.".format(user.mention)) 
