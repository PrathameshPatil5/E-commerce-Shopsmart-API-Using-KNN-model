from sqlalchemy import Column ,Integer,String,Float
from sqlalchemy.orm import relationship
from db import Base

class Product(Base):
    __tablename__="products"
    product_id=Column(Integer,primary_key=True)
    name=Column(String)
    description=Column(String)
    price=Column(Float)

    #relationship
    transactions_re=relationship('Transaction',back_populates='product_re')


