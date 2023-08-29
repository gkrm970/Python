from sqlalchemy import Column, Integer, String, ForeignKey
from product.database import Base
from sqlalchemy.orm import relationship


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, Index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey='sellers.id')
    seller = relationship("Seller", back_populates='products')


class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, Index=True)
    username = Column(String)
    details = Column(String)
    password = Column(String)
    products = relationship('Product', back_populates='Seller')
