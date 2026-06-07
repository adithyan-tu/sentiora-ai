from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from app.db.session import AsyncSessionLocal
from app.ingestion.adapters.noaa import NOAAClient
from app.ingestion.normalizers.noaa import NOAANormalizer
from app.ingestion.services.event_ingestion import EventIngestionService

RAW_DATA_DIR = Path("data/raw/noaa")


class NOAAIngestionService:
    """
    NOAA ingestion orchestration.
    """

    def __init__(self) -> None:
        self.client = NOAAClient()
        self.normalizer = NOAANormalizer()

    async def ingest_active_alerts(self) -> dict:
        response = await self.client.fetch_active_alerts()

        RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

        output_file = RAW_DATA_DIR / f"alerts_{timestamp}.json"

        with output_file.open("w", encoding="utf-8") as file:
            json.dump(
                response.model_dump(),
                file,
                indent=2,
            )

        inserted = 0
        skipped = 0

        async with AsyncSessionLocal() as db:
            ingestion_service = EventIngestionService(db)

            for feature in response.features:
                normalized_event = self.normalizer.normalize(
                    feature,
                )

                was_inserted = await ingestion_service.insert_event(
                    normalized_event,
                )

                if was_inserted:
                    inserted += 1
                else:
                    skipped += 1

            await db.commit()

        return {
            "fetched": len(response.features),
            "inserted": inserted,
            "skipped": skipped,
        }
