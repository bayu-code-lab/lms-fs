from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, customer, book_category, book

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(book_category.router, prefix="/book-categories", tags=["book categories"])
api_router.include_router(book.router, prefix="/books", tags=["books"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
