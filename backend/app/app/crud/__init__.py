from .crud_item import item
from .crud_user import user
from .crud_customer import customer
from .crud_book_category import book_category
from .crud_book import book
from .crud_book_transaction import book_transaction

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)
