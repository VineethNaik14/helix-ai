from sqlalchemy.orm import Session

from app.database.models import Repository


class RepositoryRepository:

    def get_by_path(
        self,
        db: Session,
        path: str,
    ):
        return db.query(Repository).filter(Repository.path == path).first()

    def create(
        self,
        db: Session,
        name: str,
        path: str,
        status: str,
    ):
        repository = Repository(
            name=name,
            path=path,
            status=status,
        )

        db.add(repository)
        db.commit()
        db.refresh(repository)

        return repository


repository_repository = RepositoryRepository()
