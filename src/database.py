from abc import ABC, abstractmethod
from typing import Iterable, AsyncGenerator, AsyncIterable
from datetime import datetime as dt

from async_pymongo import AsyncClient, AsyncDatabase, AsyncCollection, AsyncCursor

from config import settings
from models import Salary


class AbstractSalaryDatabase(ABC):

    @abstractmethod
    def get_salaries(self, _from: dt, to: dt) -> Iterable[dict]:
        pass


class MongoDatabase(AbstractSalaryDatabase):

    DATETIME_COLUMN = 'dt'

    def __init__(self):
        self.mongo_client: AsyncClient = AsyncClient(settings.mongo_uri)
        self.database: AsyncDatabase = self.mongo_client[settings.mongo.database]
        self.collection: AsyncCollection = self.database[settings.mongo.collection]

    async def get_salaries(self, _from: dt, to: dt) -> AsyncGenerator[Salary, None]:
        query = self._get_group_time_query(self.DATETIME_COLUMN, _from, to)
        salaries = self.collection.find(query)
        async for salary in salaries:
            yield Salary(**salary)

    @staticmethod
    def _get_group_time_query(column: str, _from: dt, to: dt) -> dict:
        return {column: {"$gte": _from, "$lt": to}}


if __name__ == '__main__':

    import asyncio

    async def check_mongo(collection):
        result = collection.find({})
        async for _ in result:
            print('Mongo works')
            break

    db = MongoDatabase()
    asyncio.run(check_mongo(db.collection))


