import datetime
from typing import Optional
from pydantic import BaseModel
from .items import ItemResponse


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    hashed_password: str


class UserUpdate(UserBase):
    hashed_password: Optional[str] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    items: list[ItemResponse] = []
    deleted_at: datetime.datetime = None

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
