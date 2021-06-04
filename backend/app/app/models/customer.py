from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Customer(Base):
    id = Column(String, primary_key=True, index=True, nullable=False)
    full_name = Column(String, index=True, nullable=False)
    grade = Column(Integer, index=True, nullable=True)
    major = Column(String, index=True, nullable=True)
    batch_of_year = Column(Integer, index=True, nullable=True)
    address = Column(String, index=True, nullable=False)
    created_by = Column(Integer, ForeignKey("user.id"), nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_by = Column(Integer, ForeignKey("user.id"), nullable=True)
    updated_date = Column(DateTime, nullable=True)