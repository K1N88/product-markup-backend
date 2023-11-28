from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.markup import Status


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
    markup: Optional[int]
    last_update: datetime
    status: Status

    class Config:
        orm_mode = True
