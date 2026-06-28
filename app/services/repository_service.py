from sqlalchemy.orm import Session

from app.database.models import Repository
from app.indexing.scanner import repository_scanner
from app.schemas.repository import RepositoryCreate


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
        scan_result = repository_scanner.scan(repository.path)

        db_repository = Repository(
            name=scan_result["name"],
            path=scan_result["path"],
            status="indexed",
        )

        db.add(db_repository)
        db.commit()
        db.refresh(db_repository)

        return {
            "id": db_repository.id,
            "name": db_repository.name,
            "status": db_repository.status,
        }


repository_service = RepositoryService()
