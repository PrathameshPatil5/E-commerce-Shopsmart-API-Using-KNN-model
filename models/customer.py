
from db import * #db contains all import and Base everything here not required to all code 
from sqlalchemy.orm import relationship 
class Customer(Base):
    __tablename__='customers'

    customer_id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String,unique=True)
    phone_number=Column(Integer,unique=True)
    location=Column(String)
    
    #relationship
    #relationship() takes class name (capitalized)
    #back_populates= refers to the attribute name in the other class


    transactions_re=relationship('Transaction',back_populates='customer_re')