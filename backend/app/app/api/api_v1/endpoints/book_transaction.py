from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[schemas.BookTransaction])
def read_book_transactions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve book_transactions.
    """
    # if crud.user.is_superuser(current_user):
    #     bookTransactions = crud.bookTransaction.get_multi(db, skip=skip, limit=limit)
    # else:
    book_transactions = crud.book_transaction.get_multi_by_owner(
        db=db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return book_transactions


@router.post("/")
def create_book_transaction(
    *,
    db: Session = Depends(deps.get_db),
    book_transaction_in: schemas.BookTransactionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new book_transaction.
    """
    book = crud.book.get(db=db, id=book_transaction_in.book_id)
    if book:
        if book.quantity <= 0:
            raise HTTPException(status_code=404, detail="Book out of stock")
    book_transaction = crud.book_transaction.create_with_owner(db=db, obj_in=book_transaction_in, owner_id=current_user.id)
    book.quantity -= book_transaction_in.total
    book.updated_by = current_user.id
    book.updated_date = str(datetime.utcnow())
    crud.book.update(db=db, db_obj=book, obj_in=book.__dict__)
    return book_transaction


@router.put("-return/{id}")
def update_book_transaction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an book_transaction.
    """
    book_transaction = crud.book_transaction.get(db=db, id=id)
    if not book_transaction:
        raise HTTPException(status_code=404, detail="BookTransaction  not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book_transaction.is_returned = True
    book_transaction.date_returned = str(datetime.utcnow())
    book_transaction.updated_by = current_user.id
    book_transaction.updated_date = str(datetime.utcnow())
    book_transaction = crud.book_transaction.update(db=db, db_obj=book_transaction, obj_in=book_transaction.__dict__)
    book = crud.book.get(db=db, id=book_transaction.book_id)
    book.quantity += book_transaction.total
    book.updated_by = current_user.id
    book.updated_date = str(datetime.utcnow())
    crud.book.update(db=db, db_obj=book, obj_in=book.__dict__)
    return book_transaction


@router.get("/{id}", response_model=schemas.BookTransaction)
def read_book_transaction(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get book_transaction by ID.
    """
    book_transaction = crud.bookTransaction.get(db=db, id=id)
    if not book_transaction:
        raise HTTPException(status_code=404, detail="Book_transaction  not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return book_transaction


# @router.delete("/{id}", response_model=schemas.BookTransaction)
# def delete_book_transaction(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an bookTransaction.
#     """
#     bookTransaction = crud.bookTransaction.get(db=db, id=id)
#     if not bookTransaction:
#         raise HTTPException(status_code=404, detail="BookTransaction  not found")
#     if not crud.user.is_superuser(current_user):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     bookTransaction = crud.bookTransaction.remove(db=db, id=id)
#     return bookTransaction
