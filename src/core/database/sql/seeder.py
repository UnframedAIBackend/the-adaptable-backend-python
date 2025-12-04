import asyncio
import os
from pathlib import Path
import asyncpg

# Load .env file manually
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

async def run_seeders():
    print("Running seeders...")
    url = os.getenv("DATABASE_URL", "").replace("+asyncpg", "")
    
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
