import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.configuration.configuration import config

async def seed():
    print("Running MongoDB seeders...")
    client = AsyncIOMotorClient(config.get("DATABASE_URL"))
    db = client.get_database()
    collection = db["notes"]
    
    notes = [
        {"content": "The only limit to our realization of tomorrow is our doubts of today."},
        {"content": "Do what you can, with what you have, where you are."}
    ]
    
    await collection.insert_many(notes)
    print("Seeded MongoDB")

if __name__ == "__main__":
    asyncio.run(seed())
