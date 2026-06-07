from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models.event import Event
from app.db.models.source import Source
from app.ingestion.schemas.normalized_event import NormalizedEvent


class EventIngestionService:
    """
    Persists normalized events into the database.
    """

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_or_create_source(
        self,
        source_name: str,
    ) -> Source:
        query = select(Source).where(
            Source.name == source_name,
        )

        result = await self.db.execute(query)

        source = result.scalar_one_or_none()

        if source:
            return source

        source = Source(
            name=source_name,
        )

        self.db.add(source)

        await self.db.flush()

        return source

    async def event_exists(
        self,
        source_id: int,
        source_event_id: str,
    ) -> bool:
        query = select(Event).where(
            Event.source_id == source_id,
            Event.source_event_id == source_event_id,
        )

        result = await self.db.execute(query)

        return result.scalar_one_or_none() is not None

    async def insert_event(
        self,
        normalized_event: NormalizedEvent,
    ) -> bool:
        source = await self.get_or_create_source(
            normalized_event.source_name,
        )

        exists = await self.event_exists(
            source.id,
            normalized_event.source_event_id,
        )

        if exists:
            return False

        event = Event(
            source_id=source.id,
            source_event_id=normalized_event.source_event_id,
            title=normalized_event.title,
            summary=normalized_event.summary,
            category=normalized_event.category,
            severity_hint=normalized_event.severity_hint,
            urgency_hint=normalized_event.urgency_hint,
            certainty_hint=normalized_event.certainty_hint,
            source_url=normalized_event.source_url,
            geometry_geojson=normalized_event.geometry_geojson,
            published_at=normalized_event.published_at,
        )

        self.db.add(event)

        return True
