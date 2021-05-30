from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from datetime import datetime
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
            print(a.__dict__)
            result.append({
                'id': a.id,
                'customer_id': b.id,
                'customer_name': b.full_name,
                'book_id': a.book_id,
                'book_title': None,
                'total': a.total,
                'day': a.day,
                'is_returned': a.is_returned,
                'date_returned':  None if  a.date_returned == None else str(a.date_returned)
            })
            
        for _ in result:
            _['book_title'] = db.query(Book).filter(Book.id == _['book_id']).first().title
        return result


book_transaction = CRUDBookTransaction(BookTransaction)