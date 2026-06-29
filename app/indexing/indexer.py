from sqlalchemy.orm import Session

from app.database.models import Class, File, Function, Repository, Import
from app.indexing.scanner import repository_scanner
from app.embeddings.embedding_service import embedding_service
from app.vectorstore.vector_service import vector_service

class RepositoryIndexer:
    def index(
        self,
        repository_path: str,
        db: Session,
    ):
        scan_result = repository_scanner.scan(repository_path)

        existing_repository = (
            db.query(Repository).filter(Repository.path == scan_result["path"]).first()
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
            db.flush()

            metadata = scan_result["python_metadata"].get(file["path"])

            if metadata:
                for function in metadata["functions"]:
                    embedding = embedding_service.embed_function(function)

                    db_function = Function(
                        file_id=db_file.id,
                        name=function["name"],
                        line=function["line"],
                        end_line=function["end_line"],
                        return_type=function["return_type"],
                        embedding=embedding,
                    )

                    db.add(db_function)
                    db.flush()

                    vector_service.index_function(
                        function_id=db_function.id,
                        function=function,
                        file_path=file["path"],
                    )

                for class_metadata in metadata["classes"]:
                    db_class = Class(
                        file_id=db_file.id,
                        name=class_metadata["name"],
                        line=class_metadata["line"],
                        end_line=class_metadata["end_line"],
                    )

                    db.add(db_class)
                
                for imported_module in metadata["imports"]:
                    db_import = Import(
                        file_id=db_file.id,
                        module=imported_module,
                    )

                    db.add(db_import)

        db.commit()

        return {
            "id": db_repository.id,
            "name": db_repository.name,
            "status": db_repository.status,
        }


repository_indexer = RepositoryIndexer()
