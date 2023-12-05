from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.markup import Choice


class MarkupCreate(BaseModel):
    key: int
    product_id: int
    create_date: datetime
    queue: int
    quality: float


class MarkupDB(MarkupCreate):
    id: int

    class Config:
        orm_mode = True


class StatisticCreate(BaseModel):
    key: int
    markup: Optional[int]
    last_update: datetime
    state: Choice


class StatisticDB(StatisticCreate):
    id: int

    class Config:
        orm_mode = True


class StatisticInfo(BaseModel):
    statistic: StatisticDB
    markup: MarkupDB

    class Config:
        orm_mode = True
