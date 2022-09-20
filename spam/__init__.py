from pyrogram import Client, filters
from config import API_ID, API_HASH, STRING_SESSION

bot = Client(
    ":spambot:",
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=STRING_SESSION, 
    plugins=dict(root="spam")
) 
