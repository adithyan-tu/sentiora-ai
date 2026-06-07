from __future__ import annotations

import asyncio

from app.ingestion.services.ingestion_runner import (
    IngestionRunner,
)


async def main() -> None:
    runner = IngestionRunner()

    result = await runner.run()

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
