from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Shared properties
class BookBase(BaseModel):
    title: str
    year: Optional[int]
    category_id: int
    category_desc: Optional[str]
    publisher: Optional[str]
    author: str
    isbn: Optional[str]
    quantity: int


# Properties to receive on Book creation
class BookCreate(BaseModel):
    title: str
    year: int
    category_id: int
    publisher: str
    author: str
    isbn: Optional[str]
    quantity: int
    
    pass


# Properties to receive on Book update
class BookUpdate(BookBase):
    pass


# Properties shared by models stored in DB
class BookInDBBase(BookBase):
    id: int
    class Config:
        orm_mode = True


# Properties to return to client
class Book(BookInDBBase):
    pass

# Properties properties stored in DB
class BookInDB(BookInDBBase):
    pass
