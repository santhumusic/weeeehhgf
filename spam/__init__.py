from pyrogram import Client, filters
from config import API_ID, API_HASH, STRING_SESSION

bot = Client(
    ":spambot:",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION("in_memory=True"), 
    plugins=dict(root="spam")
) 
