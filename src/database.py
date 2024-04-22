from abc import ABC, abstractmethod
from typing import Iterable
from datetime import datetime as dt

from async_pymongo import AsyncClient, AsyncDatabase, AsyncCollection, AsyncCursor

from config import settings


class AbstractSalaryDatabase(ABC):

    @abstractmethod
    def get_salaries(self, _from: dt, to: dt) -> Iterable[dict]:
        pass


class MongoDatabase(AbstractSalaryDatabase):

    DATETIME_COLUMN = 'dt'

    def __init__(self):
        self.mongo_client: AsyncClient = AsyncClient(settings.mongo.uri)
        self.database: AsyncDatabase = self.mongo_client[settings.mongo.database]
        self.collection: AsyncCollection = self.database[settings.mongo.collection]

    def get_salaries(self, _from: dt, to: dt) -> AsyncCursor:
        query = self._get_group_time_query(self.DATETIME_COLUMN, _from, to)
        return self.collection.find(query)

    @staticmethod
    def _get_group_time_query(column: str, _from: dt, to: dt) -> dict:
        return {column: {"gte": _from, "$lt": to}}
