from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[schemas.BookCategory])
def read_book_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve book_category.
    """
    if crud.user.is_superuser(current_user):
        book_categories = crud.book_category.get_multi(db, skip=skip, limit=limit)
    else:
        book_categories = crud.book_category.get_multi_by_owner(
            db=db, owner_id=current_user.id, skip=skip, limit=limit
        )
    return book_categories


@router.post("/", response_model=schemas.BookCategory)
def create_book_category(
    *,
    db: Session = Depends(deps.get_db),
    book_category_in: schemas.BookCategoryCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new book_category.
    """
    # if crud.book_category.get_by_customer_id(db, customer_id=customer_in.customer_id):
    #     raise HTTPException(status_code=400, detail="ID already exist")
    book_category = crud.book_category.create_with_owner(db=db, obj_in=book_category_in, owner_id=current_user.id)
    return book_category


@router.put("/{id}", response_model=schemas.BookCategory)
def update_book_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    book_category_in: schemas.BookCategoryUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an book_category.
    """
    book_category = crud.book_category.get(db=db, id=id)
    if not book_category:
        raise HTTPException(status_code=404, detail="Book Category not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book_category.updated_by = current_user.id
    book_category.updated_date = str(datetime.utcnow())
    book_category = crud.book_category.update(db=db, db_obj=book_category, obj_in=book_category_in)
    return book_category


@router.get("/{id}", response_model=schemas.BookCategory)
def read_book_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get book_category by ID.
    """
    book_category = crud.book_category.get(db=db, id=id)
    if not book_category:
        raise HTTPException(status_code=404, detail="Book Category not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return book_category


@router.delete("/{id}", response_model=schemas.BookCategory)
def delete_book_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an book_category.
    """
    book_category = crud.book_category.get(db=db, id=id)
    if not book_category:
        raise HTTPException(status_code=404, detail="Book Category not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book_category = crud.book_category.remove(db=db, id=id)
    return book_category

@router.get("ddl/", response_model=List[schemas.BookCategory])
def category_ddl(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    book_category = crud.book_category.get_category_ddl(db=db)
    return book_category
