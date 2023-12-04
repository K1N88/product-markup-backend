from datetime import date
from typing import Optional, List, Tuple

from pydantic import BaseModel, Field


class DealerBase(BaseModel):
    dealer: str

    class Config:
        orm_mode = True


class DealerDB(DealerBase):
    id: int


class DealerPriceCreate(BaseModel):
    product_key: str = Field(..., max_length=1000)
    price: str = Field(..., max_length=20)
    product_url: Optional[str] = Field(..., max_length=1000)
    product_name: str = Field(..., min_length=2, max_length=1000)
    date: date
    dealer_id: int


class DealerPriceDB(DealerPriceCreate):
    id: int

    class Config:
        orm_mode = True


class DealerPriceDealerDB(DealerBase):
    dealerprice: DealerPriceDB
    state: str = None

    class Config:
        orm_mode = True
