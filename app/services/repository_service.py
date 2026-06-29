from sqlalchemy.orm import Session

from app.schemas.repository import RepositoryCreate
from app.database.models import Repository
from app.indexing.indexer import repository_indexer

class RepositoryService:
    def list_repositories(self, db: Session):
        repositories = db.query(Repository).all()

        return [
            {
                "id": repo.id,
                "name": repo.name,
                "path": repo.path,
                "status": repo.status,
            }
            for repo in repositories
        ]

    def create_repository(
        self,
        repository: RepositoryCreate,
        db: Session,
    ):
        return repository_indexer.index(
            repository.path,
            db,
        )


repository_service = RepositoryService()
