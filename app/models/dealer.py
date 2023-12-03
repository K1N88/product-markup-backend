from sqlalchemy import Column, String, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.db import Base


class Dealer(Base):
    name = Column(String(100), unique=True, nullable=False)

    dealer_price = relationship('DealerPrice', cascade='delete',
                                back_populates="dealer")
    product_dealer_key = relationship('ProductDealerKey', cascade='delete')


class DealerPrice(Base):
    product_key = Column(String(1000),
                         nullable=False)
    price = Column('цена', String(1000), nullable=False)
    product_url = Column('адрес страницы, откуда собраны данные', String(1000))
    product_name = Column('заголовок продаваемого товара', String(1000),
                          nullable=False)
    date = Column('дата получения информации', Date, nullable=False)
    dealer_id = Column(Integer, ForeignKey('dealer.id'))

    dealer = relationship('Dealer', back_populates='dealer_price')
    product_dealer_key = relationship('ProductDealerKey', cascade='delete')
    markup = relationship('Markup', cascade='delete')
    statistic = relationship('Statistic', cascade='delete')
