from pyrogram import Client, filters
from spam.decorators import sudo_users_only
from pyrogram.types import Message
from spam.decorators import add_sudo, remove_sudo
from config import SUDO_USERS, MONGO_DB_URL, OWNER_ID
from spam import bot

@Client.on_message(filters.command(["addsudo"], [".", "/", "!"]) & OWNER_ID) 
async def useradd(client, message: Message):
    if MONGO_DB_URL is None:
        return await message.reply_text(
            "**Due to bot's privacy issues, You can't manage sudo users when you're using santhu spam Database.\n\n Please fill your MONGO_DB_URI in your vars to use this feature**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await bot.get_users(user)
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

@Client.on_message(filters.command([".delsudo"]) & OWNER_ID)
async def userdel(client, message: Message):
    if MONGO_DB_URL is None:
        return await message.reply_text(
            "**Due to bot's privacy issues, You can't manage sudo users when you're using santhu spam Database.\n\n Please fill your MONGO_DB_URI in your vars to use this feature**"
        )
    if not message.reply_to_message:
        if len(message.command) != 2:
            return await message.reply_text("Reply to a user's message or give username/user_id.")
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await bot.get_users(user)
        if user.id not in SUDO_USERS:
            return await message.reply_text("Not a part of Bot's Sudo.")
        removed = await remove_sudo(user.id)
        if removed:
            SUDO_USERS.remove(user.id)
            await message.reply_text("Removed from Bot's Sudo User")
            return
        await message.reply_text(f"Something wrong happened.")
        return
    user_id = message.reply_to_message.from_user.id
    if user_id not in SUDO_USERS:
        return await message.reply_text("Not a part of Bot's Sudo.")
    removed = await remove_sudo(user_id)
    if removed:
        SUDO_USERS.remove(user_id)
        await message.reply_text("Removed from Bot's Sudo User")
        return
    await message.reply_text(f"Something wrong happened.")


@Client.on_message(filters.command([".sudousers", ".sudolist"]) & SUDO_USERS)
async def sudoers_list(client, message: Message):
    text = "⭐️<u> **Owners:**</u>\n"
    count = 0
    for x in OWNER_ID:
        try:
            user = await bot.get_users(x)
            user = (
                user.first_name if not user.mention else user.mention
            )
            count += 1
        except Exception:
            continue
        text += f"{count}➤ {user}\n"
    smex = 0
    for user_id in SUDO_USERS:
        if user_id not in OWNER_ID:
            try:
                user = await bot.get_users(user_id)
                user = (
                    user.first_name
                    if not user.mention
                    else user.mention
                )
                if smex == 0:
                    smex += 1
                    text += "\n⭐️<u> **Sudo Users:**</u>\n"
                count += 1
                text += f"{count}➤ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("No Sudo Users")
    else:
        await message.reply_text(text)
