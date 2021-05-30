from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .customer import Customer  # noqa: F401
    from .book import Book  # noqa: F403


class BookTransaction(Base):
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("book.id"), nullable=False)
    total = Column(Integer, index=True, nullable=False)
    day = Column(Integer, index=True, nullable=False)
    is_returned = Column(Boolean(), default=False)
    date_returned = (Column(DateTime, nullable=True))
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_by = Column(Integer, ForeignKey("user.id"), nullable=True)
    updated_date = Column(DateTime, nullable=True)