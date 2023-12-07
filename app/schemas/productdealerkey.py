from pydantic import BaseModel


class ProductDealerKeyBase(BaseModel):
    pass


class ProductDealerKeyCreate(ProductDealerKeyBase):
    key: int
    dealer_id: int
    product_id: int


class ProductDealerKeyDB(ProductDealerKeyCreate):
    id: int

    class Config:
        orm_mode = True


class ProductDealerKeyBase(BaseModel):
    id: int

    class Config:
        orm_mode = True
