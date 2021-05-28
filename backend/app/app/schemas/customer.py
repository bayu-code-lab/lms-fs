from typing import Optional

from pydantic import BaseModel


# Shared properties
class CustomerBase(BaseModel):
    customer_id: str
    full_name: str
    address: str


# Properties to receive on Customer creation
class CustomerCreate(CustomerBase):
    pass


# Properties to receive on Customer update
class CustomerUpdate(CustomerBase):
    pass


# Properties shared by models stored in DB
class CustomerInDBBase(CustomerBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Customer(CustomerInDBBase):
    pass


# Properties properties stored in DB
class CustomerInDB(CustomerInDBBase):
    pass
