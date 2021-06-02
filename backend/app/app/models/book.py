from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .book_category import BookCategory  # noqa: F402


class Book(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    year = Column(Integer, index=True, nullable=True)
    category_id = Column(Integer, ForeignKey("bookcategory.id"), nullable=False)
    publisher = Column(String, index=True, nullable=True)
    author = Column(String, index=True, nullable=False)
    isbn = Column(String, index=True, nullable=True)
    quantity = Column(Integer, index=True, nullable=False)
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_by = Column(Integer, ForeignKey("user.id"), nullable=True)
    updated_date = Column(DateTime, nullable=True)