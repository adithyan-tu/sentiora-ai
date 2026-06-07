from __future__ import annotations

from app.db.session import AsyncSessionLocal
from app.ingestion.adapters.gdacs import GDACSAdapter
from app.ingestion.normalizers.gdacs import GDACSNormalizer
from app.ingestion.services.event_ingestion import (
    EventIngestionService,
)


class GDACSIngestionService:
    """
    GDACS ingestion orchestration.
    """

    def __init__(self) -> None:
        self.adapter = GDACSAdapter()
        self.normalizer = GDACSNormalizer()

    async def ingest_events(
        self,
    ) -> dict:
        events = await self.adapter.fetch_events()

        inserted = 0
        skipped = 0

        async with AsyncSessionLocal() as db:
            ingestion_service = EventIngestionService(db)

            for event in events:
                normalized = self.normalizer.normalize(
                    event,
                )

                was_inserted = await ingestion_service.insert_event(
                    normalized,
                )

                if was_inserted:
                    inserted += 1
                else:
                    skipped += 1

            await db.commit()

        return {
            "fetched": len(events),
            "inserted": inserted,
            "skipped": skipped,
        }
