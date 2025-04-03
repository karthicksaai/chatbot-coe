from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    db = None

db = Database()

async def get_database():
    return db.db

async def connect_to_mongodb():
    db.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    db.db = db.client[os.getenv("DB_NAME")]
    print("Connected to MongoDB!")

async def close_mongodb_connection():
    if db.client:
        db.client.close()
        print("MongoDB connection closed.")
