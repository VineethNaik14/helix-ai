from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description="AI Code Intelligence Platform",
        version=settings.VERSION,
    )

    app.include_router(router)

    return app
