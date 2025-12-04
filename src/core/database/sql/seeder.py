import asyncio
import os
from pathlib import Path
import asyncpg
from src.core.configuration.configuration import config

async def run_seeders():
    print("Running seeders...")
    url = config.get("DATABASE_URL").replace("+asyncpg", "")
    
    conn = await asyncpg.connect(url)
    try:
        seeders_dir = Path("src/core/database/sql/seeders")
        if not seeders_dir.exists():
            print(f"Seeders directory not found: {seeders_dir}")
            return

        for file in sorted(seeders_dir.glob("*.sql")):
            print(f"Running seeder: {file.name}")
            sql = file.read_text()
            await conn.execute(sql)
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(run_seeders())
