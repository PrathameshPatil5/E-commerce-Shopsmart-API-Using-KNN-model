from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from db import Base
class Transaction(Base):
    __tablename__="transactions"
    transaction_id=Column(Integer,primary_key=True)
    customer_id=Column(Integer,ForeignKey('customers.customer_id'))
    product_id=Column(Integer,ForeignKey('products.product_id'))
    purchase_date=Column(DateTime)

    #relationship
    customer_re=relationship('Customer',back_populates='transactions_re')
    product_re=relationship("Product" ,back_populates="transactions_re")
