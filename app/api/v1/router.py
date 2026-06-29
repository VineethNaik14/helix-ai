from fastapi import APIRouter
from app.api.v1.search import router as search_router

from app.api.v1.repositories import router as repositories_router

api_router = APIRouter()

api_router.include_router(repositories_router)
api_router.include_router(search_router)
