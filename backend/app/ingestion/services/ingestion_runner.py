from __future__ import annotations

from app.ingestion.services.gdacs_ingestion import (
    GDACSIngestionService,
)
from app.ingestion.services.noaa_ingestion import (
    NOAAIngestionService,
)


class IngestionRunner:
    """
    Runs all ingestion pipelines.
    """

    async def run(self) -> dict:
        noaa = NOAAIngestionService()

        gdacs = GDACSIngestionService()

        noaa_result = await noaa.ingest_active_alerts()

        gdacs_result = await gdacs.ingest_events()

        return {
            "NOAA": noaa_result,
            "GDACS": gdacs_result,
        }
