from pydantic import BaseModel

class customerout(BaseModel):
    customer_id:int
    name:str
    email:str
    phone_number:int
    location:str

    class config:
        orm_mode=True