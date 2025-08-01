from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from db import SessionLocal
from models.customer import Customer   #from that .py we import class which contains customer table
from Schemas.schema import customerout  

router=APIRouter()

#dependency to get session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

   


#pydantic schema for input validation
class Customercreate(BaseModel):
    name:str
    email:str
    phone_number:int
    location:str

#route to create a customer 
@router.post("/customers/")
def create_customer(customer:Customercreate,db:Session=Depends(get_db)):
    # Check if email or phone already exists
    existing = db.query(Customer).filter(  #this is query
        (Customer.email == customer.email) | (Customer.phone_number == customer.phone_number)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Customer already exists")
    
    new_customer=Customer(
        name=customer.name,
        email=customer.email,
        phone_number=customer.phone_number,
        location=customer.location
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {"message":"customer created successfully","customer_id":new_customer.customer_id}

#getting all customers
@router.get("/customers/",response_model=list[customerout])
def get_all_customers(db:Session=Depends(get_db)):
    customers=db.query(Customer).all()
    return customers

#Get customer by Id
@router.get("/customer/{customer_id}/",response_model=customerout)
def get_customer_by_id(customer_id:int,db:Session=Depends(get_db)):
    customer=db.query(Customer).filter(Customer.customer_id==customer_id).first()
    if not customer:
        raise HTTPException(status_code=404,detail='customer not found')
    return customer

