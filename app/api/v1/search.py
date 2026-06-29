from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.search_service import search_service
from app.schemas.search import SemanticSearchRequest
from app.vectorstore.vector_service import vector_service

router = APIRouter(prefix="/search", tags=["Search"])


@router.get("/functions")
async def search_functions(
    name: str,
    db: Session = Depends(get_db),
):
    return search_service.search_functions(name, db)


@router.post("/semantic")
async def semantic_search(
    request: SemanticSearchRequest,
):
    return vector_service.semantic_search(
        request.query,
    )
