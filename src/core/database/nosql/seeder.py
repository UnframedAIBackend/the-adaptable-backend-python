import asyncio
import os
from pathlib import Path
from motor.motor_asyncio import AsyncIOMotorClient

env_file = Path(".env")
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                try:
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
                except ValueError:
                    continue

async def seed():
    print("Running MongoDB seeders...")
    client = AsyncIOMotorClient(os.getenv("DATABASE_URL"))
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
