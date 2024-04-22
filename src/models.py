import json
from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from bson import ObjectId


class Salary(BaseModel):
    _id: ObjectId
    value: int
    dt: datetime


class Request(BaseModel):
    dt_from: str
    dt_upto: str
    group_type: str


class Response:

    DATASET = 'dataset'
    LABELS = 'labels'

    def __init__(self):
        self.values = []
        self.labels = []

    def add(self, label: str, value: int) -> None:
        self.labels.append(label)
        self.values.append(value)

    def __str__(self) -> str:
        return json.dumps(
            {
                self.DATASET: self.values,
                self.LABELS: self.labels
            }
        )


class GroupTypes(str, Enum):
    HOUR = 'hour'
    DAY = 'day'
    MONTH = 'month'

    @classmethod
    def values(cls):
        return cls._value2member_map_
