from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class ProductDealerKey(Base):
    key = Column('идентификатор товара', Integer,
                 ForeignKey('productdealerkey.id'))
    dealer_id = Column('идентификатор дилера', Integer,
                       ForeignKey('dealer.id'))
    product_id = Column('идентификатор продукта', Integer,
                        ForeignKey('product.id'))
