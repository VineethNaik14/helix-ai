from sqlalchemy.orm import Session

from app.database.models import Repository
from app.indexing.scanner import repository_scanner
from app.schemas.repository import RepositoryCreate
from app.database.models import File

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
        existing_repository = (
            db.query(Repository)
            .filter(Repository.path == scan_result["path"])
            .first()
        )

        if existing_repository:
            return {
                "message": "Repository already indexed",
                "id": existing_repository.id,
            }

        db_repository = Repository(
            name=scan_result["name"],
            path=scan_result["path"],
            status="indexed",
        )

        db.add(db_repository)
        db.commit()
        db.refresh(db_repository)
        for file in scan_result["files"]:
            db_file = File(
                repository_id=db_repository.id,
                path=file["path"],
                language=file["language"],
            )
            db.add(db_file)

        db.commit()

        return {
            "id": db_repository.id,
            "name": db_repository.name,
            "status": db_repository.status,
        }


repository_service = RepositoryService()
