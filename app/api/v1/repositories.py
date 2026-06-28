from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.repository import RepositoryCreate
from app.services.repository_service import repository_service

router = APIRouter(prefix="/repositories", tags=["Repositories"])


@router.get("/")
async def list_repositories(db: Session = Depends(get_db)):
    return {"repositories": repository_service.list_repositories(db)}


@router.post("/")
async def create_repository(
    repository: RepositoryCreate,
    db: Session = Depends(get_db),
):
    return repository_service.create_repository(repository, db)
