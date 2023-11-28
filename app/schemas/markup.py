from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.markup import Status


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
    last_update: datetime = datetime.now
    status: Status


class StatisticDB(StatisticCreate):
    id: int

    class Config:
        orm_mode = True
