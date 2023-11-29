from datetime import datetime
from enum import Enum as PythonEnum

from sqlalchemy import Column, DateTime, Integer, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship

from app.core.db import Base


class Choice(PythonEnum):
    YES = 'да'
    NO = 'нет'
    HOLD = 'отложить'


class Markup(Base):
    key = Column(Integer, ForeignKey('dealerprice.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    create_date = Column('дата рекомендации', DateTime, default=datetime.now)
    queue = Column('очередь', Integer, nullable=False)
    quality = Column('качество рекомендации', Float, nullable=False)

    statistic = relationship('Statistic', cascade='delete')


class Statistic(Base):
    key = Column(Integer, ForeignKey('dealerprice.id'))
    markup = Column(Integer, ForeignKey('markup.id'), nullable=True,
                    default=None)
    last_update = Column('дата обновления', DateTime, default=datetime.now)
    state = Column('статус разметки', Enum(Choice))
