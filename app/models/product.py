from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from app.core.db import Base


class Product(Base):
    article = Column('артикул товара', String(100), unique=True,
                     nullable=False)
    ean_13 = Column('код товара', Integer)
    name = Column('название товара', String(1000))
    cost = Column('стоимость', Float)
    min_recommended_price = Column('рекомендованная минимальная цена', Float)
    recommended_price = Column('рекомендованная цена', Float)
    category_id = Column('категория товара', Integer)
    ozon_name = Column('названиет товара на Озоне', String(1000))
    name_1c = Column('название товара в 1C', String(1000))
    wb_name = Column('название товара на Wildberries', String(1000))
    ozon_article = Column('описание для Озон', Integer)
    wb_article = Column('артикул для Wildberries', Integer)
    wb_article_td = Column('артикул для Wildberries td', String(100))
    ym_article = Column('артикул для Яндекс.Маркета', String(100))
