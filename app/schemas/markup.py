from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MarkupDB(BaseModel):
    id: int
    key: int
    product_id: int
    create_date: datetime
    queue: int
    quality: float

    class Config:
        orm_mode = True


class StatisticDB(BaseModel):
    id: int
    key: int
    markup: int
    last_update: datetime

    class Config:
        orm_mode = True
