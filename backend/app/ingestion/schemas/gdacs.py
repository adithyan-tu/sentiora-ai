from __future__ import annotations

from pydantic import BaseModel


class GDACSEvent(BaseModel):
    event_id: str

    title: str

    link: str

    summary: str | None = None

    category: str | None = None

    alert_level: str | None = None

    published_at: str | None = None

    latitude: float | None = None

    longitude: float | None = None
