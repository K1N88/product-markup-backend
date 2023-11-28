from sqlalchemy import Column, String, Date, ForeignKey, Integer, Float
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.db import Base


class Dealer(Base):
    name = Column(String(100), unique=True, nullable=False)
    dealer_price = relationship('DealerPrice', cascade='delete')


class DealerPrice(Base):
    __table_args__ = (
        UniqueConstraint('уникальный номер позиции', 'идентификатор дилера',
                         name="product_dealer"),
    )

    product_key = Column('уникальный номер позиции', Integer, nullable=False)
    price = Column('цена', Float, nullable=False)
    product_url = Column('адрес страницы, откуда собраны данные', String(1000))
    product_name = Column('заголовок продаваемого товара', String(1000),
                          nullable=False)
    date = Column('дата получения информации', Date, nullable=False)
    dealer_id = Column('идентификатор дилера', Integer,
                       ForeignKey('dealer.id'))
