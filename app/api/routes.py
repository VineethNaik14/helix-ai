from fastapi import APIRouter

from app.api.v1.router import api_router
from app.core.config import settings

router = APIRouter()

router.include_router(api_router, prefix="/api/v1")


@router.get("/", tags=["Root"])
async def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.VERSION,
    }


@router.get("/health", tags=["Health"])
async def health():
    return {"status": "healthy"}
