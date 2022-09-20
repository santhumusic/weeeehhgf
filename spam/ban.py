from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message
from spam import bot
import logging
from pyrogram.types import *
from config import SUDO_USERS

SUDO_USERS = SUDO_USERS

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.command(["banall"], [".", "/", "!"])) 
async def banall(client: Client, message: Message):
    logging.info("new chat {}".format(message.chat.id))
    logging.info("getting memebers from {}".format(message.chat.id))
    member = client.get_chat_members(message.chat.id)
    for alls in member:
        try:
            bot.kick_chat_member(chat_id =message.chat.id,user_id=alls.user.id)
            logging.info("kicked {} from {}".format(alls.user.id,message.chat.id))
        except Exception:
            logging.info("failed to kicked {} from {}".format(alls.user.id,message.chat.id))
            
    logging.info("process completed")

