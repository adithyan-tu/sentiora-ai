from __future__ import annotations

import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

DEFAULT_TIMEOUT = 30.0


class BaseAPIClient:
    """
    Shared async HTTP client for external APIs.
    """

    def __init__(self, base_url: str, user_agent: str) -> None:
        self.base_url = base_url
        self.headers = {
            "User-Agent": user_agent,
            "Accept": "application/json",
        }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        reraise=True,
    )
    async def get_json(self, endpoint: str) -> dict:
        timeout = httpx.Timeout(DEFAULT_TIMEOUT)

        async with httpx.AsyncClient(
            base_url=self.base_url,
            headers=self.headers,
            timeout=timeout,
        ) as client:
            response = await client.get(endpoint)

            response.raise_for_status()

            return response.json()
