from datetime import date
from typing import Optional

from pydantic import BaseModel, Extra, Field


class DealerDB(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=100, title='Имя дилера')


class DealersCreate(BaseModel):
    data: list[DealerDB]


class DealerPriceCreate(BaseModel):
    product_key: int
    price: float = Field(..., gt=0)
    product_url: Optional[str] = Field(..., max_length=1000)
    product_name: str = Field(..., min_length=2, max_length=1000,)
    date: date
    dealer_id: int

    class Config:
        orm_mode = True
