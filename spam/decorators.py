from pyrogram import Client, filters
from config import SUDO_USERS
from typing import Callable
from pyrogram.types import Message

def sudo_users_only(func: Callable) -> Callable:
    async def decorator(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)
        
    return decorator
