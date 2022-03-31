import datetime
from typing import Optional
from pydantic import BaseModel
from .items import ItemResponse


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    items: list[ItemResponse] = []
    deleted_at: datetime.datetime = None

    class Config:
        orm_mode = True