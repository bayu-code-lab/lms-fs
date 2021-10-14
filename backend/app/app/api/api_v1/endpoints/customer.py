from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[schemas.Customer])
def read_customers(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 10000,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve customers.
    """
    if crud.user.is_superuser(current_user):
        customers = crud.customer.get_multi(db, skip=skip, limit=limit)
    else:
        customers = crud.customer.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return customers

@router.get("-search")
def search_customer(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    customers = crud.customer.customer_search(
        db=db, owner_id=current_user.id
    )
    return customers

@router.post("/", response_model=schemas.Customer)
def create_customer(
    *,
    db: Session = Depends(deps.get_db),
    customer_in: schemas.CustomerCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new customer.
    """
    if crud.customer.get_by_customer_id(db, id=customer_in.id):
        raise HTTPException(status_code=400, detail="NIK/NISN sudah terdaftar di database")
    customer = crud.customer.create_with_owner(db=db, obj_in=customer_in, owner_id=current_user.id)
    return customer


@router.put("/{id}", response_model=schemas.Customer)
def update_customer(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    customer_in: schemas.CustomerUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an customer.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if not crud.user.is_superuser(current_user): #and (customer.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    customer.updated_by = current_user.id
    customer.updated_date = str(datetime.utcnow())
    customer = crud.customer.update(db=db, db_obj=customer, obj_in=customer_in)
    return customer


@router.get("/{id}", response_model=schemas.Customer)
def read_customer(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get customer by ID.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if not crud.user.is_superuser(current_user) and (customer.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return customer


@router.delete("/{id}", response_model=schemas.Customer)
def delete_customer(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an customer.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    if not crud.user.is_superuser(current_user) and (customer.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    customer = crud.customer.remove(db=db, id=id)
    return customer
