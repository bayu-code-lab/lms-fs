from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[schemas.Book])
def read_books(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve books.
    """
    # if crud.user.is_superuser(current_user):
    #     books = crud.book.get_multi(db, skip=skip, limit=limit)
    # else:
    books = crud.book.get_multi_by_owner(
        db=db, owner_id=current_user.id, skip=skip, limit=limit
    )
    return books

@router.get("-search")
def search_book(
    db: Session = Depends(deps.get_db),
    book_title: str = '',
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    books = crud.book.book_search(
        db=db, owner_id=current_user.id, book_title=book_title
    )
    return books

@router.post("/", response_model=schemas.Book)
def create_book(
    *,
    db: Session = Depends(deps.get_db),
    book_in: schemas.BookCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new book.
    """
    # if crud.book.get_by_customer_id(db, customer_id=customer_in.customer_id):
    #     raise HTTPException(status_code=400, detail="ID already exist")
    book = crud.book.create_with_owner(db=db, obj_in=book_in, owner_id=current_user.id)
    return book


@router.put("/{id}", response_model=schemas.Book)
def update_book(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    book_in: schemas.BookUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an book.
    """
    book = crud.book.get(db=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book  not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book.updated_by = current_user.id
    book.updated_date = str(datetime.utcnow())
    book = crud.book.update(db=db, db_obj=book, obj_in=book_in)
    return book


@router.get("/{id}", response_model=schemas.Book)
def read_book(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get book by ID.
    """
    book = crud.book.get(db=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book  not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return book


@router.delete("/{id}", response_model=schemas.Book)
def delete_book(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an book.
    """
    book = crud.book.get(db=db, id=id)
    if not book:
        raise HTTPException(status_code=404, detail="Book  not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book = crud.book.remove(db=db, id=id)
    return book
