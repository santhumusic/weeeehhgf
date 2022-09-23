from pyrogram import Client, filters
from spam.decorators import sudo_users_only
from pyrogram.types import Message
from spam.decorators import add_sudo, remove_sudo


@Client.on_message(filters.command(["addsudo"], [".", "/", "!"]))
@sudo_users_only
async def addsudo(client, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        if user.id in SUDO_USERS:
            return await message.reply_text(
                "{0} is already a sudo user.".format(user.mention)
            )
        added = await add_sudo(user.id)
        if added:
            SUDO_USERS.add(user.id)
            await message.reply_text("Added **{0}** to Sudo Users.".format(user.mention))
        else:
            await message.reply_text("Failed")
        return
    if message.reply_to_message.from_user.id in SUDO_USERS:
        return await message.reply_text(
            "{0} is already a sudo user.".format(
                message.reply_to_message.from_user.mention
            )
        )
    added = await add_sudo(message.reply_to_message.from_user.id)
    if added:
        SUDO_USERS.add(message.reply_to_message.from_user.id)
        await message.reply_text(
            "Added **{0}** to Sudo Users.".format(
                message.reply_to_message.from_user.mention
            )
        )
    else:
        await message.reply_text("Failed")
    return

