from pyrogram import Client, filters
from config import API_ID, API_HASH, STRING_SESSION

bot = Client(
    ":spambot:",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION, 
    plugins=dict(root="spam")
) 

# Database

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client
from config import MONGO_DB_URL
from spam.logger import LOGGER


_mongo_async_ = _mongo_client_(MONGO_DB_URL)
_mongo_sync_ = MongoClient(MONGO_DB_URL)

mongodb = _mongo_async_.spam
pymongodb = _mongo_sync_.spam

dbb = _mongo_async_["SANTHUDB"]
