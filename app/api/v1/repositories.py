from fastapi import APIRouter

from app.schemas.repository import RepositoryCreate
from app.services.repository_service import repository_service

router = APIRouter(prefix="/repositories", tags=["Repositories"])


@router.get("/")
async def list_repositories():
    return {"repositories": repository_service.list_repositories()}


@router.post("/")
async def create_repository(repository: RepositoryCreate):
    return repository_service.create_repository(repository)
