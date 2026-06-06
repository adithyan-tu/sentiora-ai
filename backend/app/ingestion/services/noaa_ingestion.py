from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path

from app.ingestion.adapters.noaa import NOAAClient

RAW_DATA_DIR = Path("data/raw/noaa")


class NOAAIngestionService:
    """
    Handles NOAA ingestion workflow.
    """

    def __init__(self) -> None:
        self.client = NOAAClient()

    async def ingest_active_alerts(self) -> int:
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

        return len(response.features)
