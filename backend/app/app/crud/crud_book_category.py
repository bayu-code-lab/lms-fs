from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime
from app.crud.base import CRUDBase
from app.models.book_category import BookCategory
from app.schemas.book_category import BookCategoryCreate, BookCategoryUpdate


class CRUDBookCategory(CRUDBase[BookCategory, BookCategoryCreate, BookCategoryUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: BookCategoryCreate, owner_id: int
    ) -> BookCategory:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, created_by=owner_id, created_date=datetime.utcnow())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[BookCategory]:
        return (
            db.query(self.model)
            .offset(skip)
            .limit(limit)
            .all()
        )
        
    def get_category_ddl(self, db: Session):
        return db.query(BookCategory).all()


book_category = CRUDBookCategory(BookCategory)