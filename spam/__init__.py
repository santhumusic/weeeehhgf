from pyrogram import Client, filters
from config import API_ID, API_HASH

bot = Client(
    ":spambot:",
    api_id=API_ID,
    api_hash=API_HASH,
    in_memory=session_string, 
    plugins=dict(root="spam")
) 
