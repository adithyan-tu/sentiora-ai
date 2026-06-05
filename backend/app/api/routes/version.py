from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()


@router.get("/version")
async def version() -> dict:
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
    }