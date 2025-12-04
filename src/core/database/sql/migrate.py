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

async def run_migrations():
    print("Running migrations...")
    url = os.getenv("DATABASE_URL", "").replace("+asyncpg", "")
    
    conn = await asyncpg.connect(url)
    try:
        migrations_dir = Path("src/core/database/sql/migrations")
        # Ensure directory exists
        if not migrations_dir.exists():
            print(f"Migrations directory not found: {migrations_dir}")
            return

        for file in sorted(migrations_dir.glob("*.sql")):
            print(f"Running migration: {file.name}")
            sql = file.read_text()
            await conn.execute(sql)
    finally:
        await conn.close()

if __name__ == "__main__":
    asyncio.run(run_migrations())
