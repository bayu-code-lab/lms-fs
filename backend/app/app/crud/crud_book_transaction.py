from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.crud.base import CRUDBase
from app.models.book_transaction import BookTransaction
from app.models.book import Book
from app.models.customer import Customer
from app.schemas.book_transaction import BookTransactionCreate, BookTransactionUpdate


class CRUDBookTransaction(CRUDBase[BookTransaction, BookTransactionCreate, BookTransactionUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: BookTransactionCreate, owner_id: int
    ) -> BookTransaction:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, created_by=owner_id, created_date=datetime.utcnow())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[BookTransaction]:
        result = list()
        
        for a, b in db.query(self.model, Customer).filter(self.model.customer_id == Customer.id, self.model.is_returned == False).offset(skip).limit(limit).all():
            created_date = a.created_date + timedelta(hours=7)
            is_late = True if (created_date + timedelta(days=a.day)) < (datetime.utcnow() + timedelta(hours=7)) else False
            result.append({
                'id': a.id,
                'customer_id': b.id,
                'customer_name': b.full_name,
                'book_id': a.book_id,
                'book_title': None,
                'year': None,
                'publisher': None,
                'total': a.total,
                'day': a.day,
                'is_returned': a.is_returned,
                'is_late': is_late,
                'date_returned':  None if  a.date_returned == None else (a.date_returned + timedelta(hours=7)).strftime("%b %d %Y %H:%M:%S"),
                'created_date':  created_date.strftime("%b %d %Y %H:%M:%S")
            })
            
        for _ in result:
            data = db.query(Book).filter(Book.id == _['book_id']).first()
            _['book_title'] = data.title
            _['year'] =  data.year
            _['publisher'] = data.publisher
        return result


book_transaction = CRUDBookTransaction(BookTransaction)