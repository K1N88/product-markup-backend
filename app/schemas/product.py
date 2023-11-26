from pydantic import BaseModel, Extra

class ProductBase(BaseModel):
    article: str
    name: str
    cost: float
    min_recommended_price: float
    recommended_price: float
    category_id: int
    ozon_name: str
    name_1c: str
    wb_name: str
    ozon_article: int
    wb_article: int
    wb_article_td: str
    ym_article: str

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