from pydantic import BaseModel, Extra
from typing import Optional


class ProductDealerKeyBase(BaseModel):
    pass


class ProductDealerKeyCreate(ProductDealerKeyBase):
    product_id: int
    dealer_id: int

    class Config:
        extra = Extra.forbid


class ProductDealerKeyDB(ProductDealerKeyBase):
    id: int