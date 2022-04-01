from fastapi import APIRouter, Depends, HTTPException
from app.schemas.items import ItemResponse, ItemCreate
from app.crud.items import crud_items
from .dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=list[ItemResponse])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud_items.get_list(db, skip=skip, limit=limit)
    return items


@router.post("", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return crud_items.create_user_item(db=db, item=item, user_id=1)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_db)):
    db_user = crud_items.get(db, id=item_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_user


@router.delete("/{item_id}")
def remove_item(item_id: int, db: Session = Depends(get_db)):
    db_user = crud_items.remove(db, id=item_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {'msg': 'success'}