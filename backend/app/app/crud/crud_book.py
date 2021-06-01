from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime
from app.crud.base import CRUDBase
from app.models.book import Book
from app.models.book_category import BookCategory
from app.schemas.book import BookCreate, BookUpdate
from sqlalchemy import func


class CRUDBook(CRUDBase[Book, BookCreate, BookUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: BookCreate, owner_id: int
    ) -> Book:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, created_by=owner_id, created_date=datetime.utcnow())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Book]:
        result = list()
        for a, b in db.query(self.model, BookCategory).filter(self.model.category_id == BookCategory.id).offset(skip).limit(limit).all():
            result.append({
                'id': a.id,
                'title': a.title,
                'desc': a.desc,
                'category_id': a.category_id,
                'category_desc': b.desc,
                'author': a.author,
                'quantity': a.quantity
            })
        return result
    
    def book_search(
        self, db: Session, *, owner_id: int, book_title: str
    ) -> List[Book]:
        result = dict()
        entries = list()
        if book_title == '':
            for a, b in db.query(self.model, BookCategory).filter(self.model.category_id == BookCategory.id).all():
                entries.append({
                    'id': a.id,
                    'title': a.title,
                    'desc': a.desc,
                    'category_id': a.category_id,
                    'category_desc': b.desc,
                    'author': a.author,
                    'quantity': a.quantity
                })
                result['count'] = len(entries)
                result['entries'] = entries
        else:
            for a, b in db.query(self.model, BookCategory).filter(self.model.category_id == BookCategory.id, func.lower(self.model.title).like('%{}%'.format(book_title.lower()))).limit(20).all():
                entries.append({
                    'id': a.id,
                    'title': a.title,
                    'desc': a.desc,
                    'category_id': a.category_id,
                    'category_desc': b.desc,
                    'author': a.author,
                    'quantity': a.quantity
                })
                result['count'] = len(entries)
                result['entries'] = entries
        return result
        
    # def get_by_book_id(self, db: Session, *, book_id: str):
    #     return db.query(Book).filter(Book.Book_id == Book_id).first() is not None


book = CRUDBook(Book)