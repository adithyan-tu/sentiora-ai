from __future__ import annotations

import pytest

from app.ingestion.adapters.noaa import NOAAClient


@pytest.mark.asyncio
async def test_fetch_active_alerts(httpx_mock) -> None:
    mock_response = {
        "features": [
            {
                "id": "test-alert",
                "properties": {
                    "event": "Tornado Warning",
                    "severity": "Severe",
                },
            }
        ]
    }

    httpx_mock.add_response(json=mock_response)

    client = NOAAClient()

    response = await client.fetch_active_alerts()

    assert len(response.features) == 1

    assert response.features[0].properties.event == "Tornado Warning"
