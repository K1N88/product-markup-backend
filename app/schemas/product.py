from typing import Optional

from pydantic import BaseModel, Extra


class ProductBase(BaseModel):
    article: str
    name: Optional[str]
    cost: Optional[str]
    min_recommended_price: Optional[str]
    recommended_price: Optional[str]
    category_id: Optional[str]
    ozon_name: Optional[str]
    name_1c: Optional[str]
    wb_name: Optional[str]
    ozon_article: Optional[str]
    wb_article: Optional[str]
    wb_article_td: Optional[str]
    ym_article: Optional[str]


class ProductCreate(ProductBase):
    class Config:
        extra = Extra.forbid


class ProductUpdate(ProductBase):
    class Config:
        extra = Extra.forbid


class ProductDB(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductM(BaseModel):
    id: int
    article: str
    name: Optional[str]

    class Config:
        orm_mode = True
