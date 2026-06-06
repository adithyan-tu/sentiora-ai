from __future__ import annotations

from app.ingestion.clients.base import BaseAPIClient
from app.ingestion.schemas.noaa import NOAAAlertsResponse


class NOAAClient(BaseAPIClient):
    """
    NOAA/NWS alerts client.
    """

    def __init__(self) -> None:
        super().__init__(
            base_url="https://api.weather.gov",
            user_agent="sentiora-ai/0.1.0",
        )

    async def fetch_active_alerts(self) -> NOAAAlertsResponse:
        payload = await self.get_json("/alerts/active")

        return NOAAAlertsResponse.model_validate(payload)
