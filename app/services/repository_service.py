from app.indexing.scanner import repository_scanner
from app.schemas.repository import RepositoryCreate


class RepositoryService:
    def list_repositories(self):
        return []

    def create_repository(self, repository: RepositoryCreate):
        return repository_scanner.scan(repository.path)


repository_service = RepositoryService()
