from datetime import UTC, datetime

from fastapi import APIRouter
from sqlalchemy import text

from app.core.config import settings
from app.db.session import engine

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    db_status = "unknown"

    try:
        async with engine.begin() as connection:
            await connection.execute(text("SELECT 1"))
            db_status = "connected"

    except Exception:
        db_status = "disconnected"

    return {
        "status": "ok",
        "database": db_status,
        "environment": settings.APP_ENV,
        "timestamp": datetime.now(UTC).isoformat(),
    }