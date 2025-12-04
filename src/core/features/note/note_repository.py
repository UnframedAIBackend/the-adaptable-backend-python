from src.core.database.i_repository import IRepository
from src.core.database.database_engine import DatabaseEngine
from src.core.configuration.configuration import config
from src.core.database.sql.sql_repository import SQLRepository
from src.core.database.nosql.nosql_repository import NoSQLRepository

class NoteRepository:
    def __init__(self):
        db_engine = config.get("DATABASE_ENGINE")
        self.repository: IRepository
        
        if db_engine == DatabaseEngine.SQL:
            self.repository = SQLRepository("notes")
        elif db_engine == DatabaseEngine.NOSQL:
            self.repository = NoSQLRepository("notes")

    async def find_all(self):
        return await self.repository.find_all()
        
    async def create(self, data):
        return await self.repository.create(data)

    async def find_by_id(self, id):
        return await self.repository.find_by_id(id)

    async def update(self, id, data):
        return await self.repository.update(id, data)

    async def delete(self, id):
        return await self.repository.delete(id)
