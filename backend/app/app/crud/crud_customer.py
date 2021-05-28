from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerUpdate


class CRUDCustomer(CRUDBase[Customer, CustomerCreate, CustomerUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: CustomerCreate, owner_id: int
    ) -> Customer:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, owner_id=owner_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, owner_id: int, skip: int = 0, limit: int = 100
    ) -> List[Customer]:
        return (
            db.query(self.model)
            .filter(Customer.owner_id == owner_id)
            .offset(skip)
            .limit(limit)
            .all()
        )
        
    def get_by_customer_id(self, db: Session, *, customer_id: str):
        return db.query(Customer).filter(Customer.customer_id == customer_id).first() is not None


customer = CRUDCustomer(Customer)