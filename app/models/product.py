from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Product(Base):
    article = Column('артикул товара', String(100), unique=True,
                     nullable=False)
    ean_13 = Column('код товара', String(100))
    name = Column('название товара', String(1000))
    cost = Column('стоимость', String(100))
    recommended_price = Column('рекомендованная цена', String(100))
    category_id = Column('категория товара', String(100))
    ozon_name = Column('название товара на Озоне', String(1000))
    name_1c = Column('название товара в 1C', String(1000))
    wb_name = Column('название товара на Wildberries', String(1000))
    ozon_article = Column('описание для Озон', String(100))
    wb_article = Column('артикул для Wildberries', String(100))
    wb_article_td = Column('артикул для Wildberries td', String(100))
    ym_article = Column('артикул для Яндекс.Маркета', String(100))

    product_dealer_key = relationship('ProductDealerKey',
                                      back_populates='product')
    markup = relationship('Markup', back_populates='product')
