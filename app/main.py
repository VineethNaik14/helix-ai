from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Code Intelligence Platform",
    version=settings.VERSION,
)


@app.get("/", tags=["Root"])
async def root():
    return {
        "project": settings.APP_NAME,
        "version": settings.VERSION,
    }


@app.get("/health", tags=["Health"])
async def health():
    return {"Status": "Healthy"}
