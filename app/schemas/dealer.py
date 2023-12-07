from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.product import ProductM


class DealerCreate(BaseModel):
    name: str


class DealerBase(DealerCreate):
    id: int

    class Config:
        orm_mode = True


class DealerDB(BaseModel):
    dealer: str

    class Config:
        orm_mode = True


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


class DealerPriceDealerDB(DealerDB):
    dealerprice: DealerPriceDB
    state: str = None
    product: ProductM = None
