from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Shared properties
class BookCategoryBase(BaseModel):
    desc: str


# Properties to receive on BookCategory creation
class BookCategoryCreate(BookCategoryBase):
    pass


# Properties to receive on BookCategory update
class BookCategoryUpdate(BookCategoryBase):
    pass


# Properties shared by models stored in DB
class BookCategoryInDBBase(BookCategoryBase):
    id: int
    created_by: int
    created_date: datetime
    updated_by: Optional[int]
    updated_date: Optional[datetime]
    class Config:
        orm_mode = True


# Properties to return to client
class BookCategory(BookCategoryInDBBase):
    pass


# Properties properties stored in DB
class BookCategoryInDB(BookCategoryInDBBase):
    pass
