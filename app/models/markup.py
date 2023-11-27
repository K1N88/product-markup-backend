from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, ForeignKey, Float

from app.core.db import Base


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
    last_update = Column('дата hfpvtnrb', DateTime, default=datetime.now)
