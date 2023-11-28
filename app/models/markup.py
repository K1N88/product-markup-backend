from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, ForeignKey, Float, Enum

from app.core.db import Base


class Status(str, Enum):
    YES = 'да'
    NO = 'нет'
    HOLD = 'отложить'


class Markup(Base):
    key = Column('идентификатор товара', Integer,
                 ForeignKey('productdealerkey.id'))
    product_id = Column('идентификатор продукта', Integer,
                        ForeignKey('product.id'))
    create_date = Column('дата рекомендации', DateTime, default=datetime.now)
    queue = Column('очередь', Integer, nullable=False)
    quality = Column('качество рекомендации', Float, nullable=False)


class Statistic(Base):
    key = Column('идентификатор товара', Integer,
                 ForeignKey('productdealerkey.id'))
    markup = Column('идентификатор продукта из рекомендации', Integer,
                    ForeignKey('markup.id'), nullable=True, default=None)
    last_update = Column('дата обновления', DateTime)
    status = Column('статус разметки', Status)
