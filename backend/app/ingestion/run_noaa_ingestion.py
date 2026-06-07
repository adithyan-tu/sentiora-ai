from __future__ import annotations

import asyncio

from app.ingestion.services.noaa_ingestion import NOAAIngestionService


async def main() -> None:
    service = NOAAIngestionService()

    result = await service.ingest_active_alerts()

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
