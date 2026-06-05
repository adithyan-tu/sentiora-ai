from datetime import datetime

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Event(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)

    source_id: Mapped[int] = mapped_column(
        ForeignKey("sources.id"),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    source_url: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    published_at: Mapped[datetime | None]

    created_at: Mapped[datetime] = mapped_column(
        default=datetime.utcnow,
    )
