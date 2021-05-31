from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Shared properties
class BookTransactionBase(BaseModel):
    customer_id: int
    customer_name: Optional[str]
    book_id: int
    book_title: Optional[str]
    total: int
    day: int
    is_returned: bool
    is_late: Optional[bool]
    date_returned: Optional[str]
    created_date: Optional[str]


# Properties to receive on BookTransaction creation
class BookTransactionCreate(BaseModel):
    customer_id: int
    book_id: int
    total: int
    day: int


# Properties to receive on BookTransaction update
class BookTransactionUpdate(BookTransactionBase):
    pass


# Properties shared by models stored in DB
class BookTransactionInDBBase(BookTransactionBase):
    id: int
    class Config:
        orm_mode = True


# Properties to return to client
class BookTransaction(BookTransactionInDBBase):
    pass


# Properties properties stored in DB
class BookTransactionInDB(BookTransactionInDBBase):
    pass
