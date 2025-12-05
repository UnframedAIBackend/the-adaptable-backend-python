import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from src.core.configuration.configuration import config


class NoSQLSeeder:
    def __init__(self):
        self.database_url = config.get("DATABASE_URL")
    
    async def run(self) -> None:
        print("Running MongoDB seeders...")
        
        try:
            client = AsyncIOMotorClient(self.database_url)
            db = client.get_database()
            collection = db["notes"]
            
            notes = [
                {"content": "The only limit to our realization of tomorrow is our doubts of today."},
                {"content": "Do what you can, with what you have, where you are."}
            ]
            
            await collection.insert_many(notes)
            print("✓ Seeded MongoDB successfully")
        except Exception as e:
            print(f"✗ MongoDB Seeder failed: {e}")
            raise

if __name__ == "__main__":
    seeder = NoSQLSeeder()
    asyncio.run(seeder.run())
