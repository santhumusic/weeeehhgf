from pyrogram import Client, filters
from config import API_ID, API_HASH, STRING_SESSION

bot = Client(
    ":spambot:",
    API_ID,
    API_HASH,
    STRING_SESSION=STRING_SESSION,
    in_memory=True, 
    plugins=dict(root="spam")
) 
