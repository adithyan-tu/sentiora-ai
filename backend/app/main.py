import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.core.metadata import APP_METADATA

setup_logging()

logger = logging.getLogger(__name__)


def create_application() -> FastAPI:
    logger.info("Initializing Sentiora AI backend")

    app = FastAPI(**APP_METADATA)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    logger.info("Application initialized successfully")

    return app


app = create_application()
