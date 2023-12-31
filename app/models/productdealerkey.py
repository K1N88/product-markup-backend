from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class ProductDealerKey(Base):
    key = Column(Integer, ForeignKey('dealerprice.id'))
    dealer_id = Column(Integer, ForeignKey('dealer.id'))
    product_id = Column(Integer, ForeignKey('product.id'))

    dealer = relationship('Dealer', back_populates='product_dealer_key')
    product = relationship('Product', back_populates='product_dealer_key')
    price = relationship('DealerPrice', back_populates='product_dealer_key')
