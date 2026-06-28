from pydantic import BaseModel, HttpUrl


class RepositoryCreate(BaseModel):
    path : str


class RepositoryResponse(BaseModel):
    id: int
    github_url: HttpUrl
    status: str
