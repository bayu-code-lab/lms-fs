from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


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
    created_by: int
    created_date: datetime
    updated_by: Optional[int]
    updated_date: Optional[datetime]
    class Config:
        orm_mode = True


# Properties to return to client
class Customer(CustomerInDBBase):
    pass


# Properties properties stored in DB
class CustomerInDB(CustomerInDBBase):
    pass
