from datetime import UTC, datetime

from sqlalchemy import JSON, DateTime, ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Event(Base):
    __tablename__ = "events"

    __table_args__ = (
        UniqueConstraint(
            "source_id",
            "source_event_id",
            name="uq_source_event",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    source_id: Mapped[int] = mapped_column(
        ForeignKey("sources.id"),
        nullable=False,
    )

    source_event_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    summary: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    category: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    severity_hint: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    urgency_hint: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    certainty_hint: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    source_url: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    geometry_geojson: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )

    published_at = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    created_at = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(UTC),
    )
