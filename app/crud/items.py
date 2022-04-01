from sqlalchemy.orm import Session
from app.models.items import Item
from app.schemas.items import ItemCreate, ItemUpdate
from app.crud.crud_base import CrudBase


class CrudItem(CrudBase[Item, ItemCreate, ItemUpdate]):

    def create_user_item(self, db: Session, item: ItemCreate, user_id: int):
        db_item = Item(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item


crud_items = CrudItem(Item)