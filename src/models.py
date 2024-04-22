import json
from datetime import datetime

from pydantic import BaseModel
from bson import ObjectId


class Salary(BaseModel):
    _id: ObjectId
    value: int
    dt: datetime


class Response:

    DATASET = 'dataset'
    LABELS = 'labels'

    def __init__(self):
        self.values = []
        self.labels = []

    def add(self, label: str, value: str) -> None:
        self.labels.append(label)
        self.values.append(value)

    def __str__(self) -> str:
        return json.dumps(
            {
                self.DATASET: self.values,
                self.LABELS: self.labels
            }
        )
