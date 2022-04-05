from fastapi import APIRouter
from app.api import users, items, authentication

api_router = APIRouter()
api_router.include_router(authentication.router, tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
