import asyncio
import os
from pathlib import Path
import asyncpg
from src.core.configuration.configuration import config

async def run_migrations():
    print("Running migrations...")
    url = config.get("DATABASE_URL").replace("+asyncpg", "")
    
    conn = await asyncpg.connect(url)
    try:
        migrations_dir = Path("src/core/database/sql/migrations")
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
