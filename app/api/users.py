from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.users import UserResponse, UserCreate, UserUpdate
from app.schemas.items import ItemResponse, ItemCreate
from app.crud.users import crud_users
from app.crud.items import crud_items
from .dependencies import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud_users.get_list(db, skip=skip, limit=limit)
    return users


@router.post("", response_model=UserResponse, status_code=status.HTTP_200_OK)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_users.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_users.crud_create_user(db=db, user=user)


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_users.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud_users.get(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud_users.update(db=db, db_obj=db_user, obj_in=user)


@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud_users.remove(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {'msg': 'success'}


@router.post("/{user_id}/items", response_model=ItemResponse)
def create_item_for_user(
    user_id: int, item: ItemCreate, db: Session = Depends(get_db)
):
    return crud_items.create_user_item(db=db, item=item, user_id=user_id)
