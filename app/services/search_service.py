from sqlalchemy.orm import Session

from app.database.models import File, Function


class SearchService:
    def search_functions(
        self,
        name: str,
        db: Session,
    ):
        functions = (
            db.query(Function, File)
            .join(File, Function.file_id == File.id)
            .filter(Function.name.ilike(f"%{name}%"))
            .all()
        )

        return [
            {
                "function": function.name,
                "file": file.path,
                "line": function.line,
                "return_type": function.return_type,
            }
            for function, file in functions
        ]


search_service = SearchService()
