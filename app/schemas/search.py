from pydantic import BaseModel


class SemanticSearchRequest(BaseModel):
    query: str


class SemanticSearchResult(BaseModel):
    name: str
    file: str
    line: int
    score: float
