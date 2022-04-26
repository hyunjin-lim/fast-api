from fastapi import APIRouter, Depends
from app.api import users, items, authentication
from app.api.dependencies import get_current_user

api_router = APIRouter()
api_router.include_router(authentication.router, tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"], dependencies=[Depends(get_current_user)])
api_router.include_router(items.router, prefix="/items", tags=["items"])
