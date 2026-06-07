from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel


class NormalizedEvent(BaseModel):
    source_name: str

    source_event_id: str

    title: str

    summary: str | None = None

    category: str | None = None

    severity_hint: str | None = None

    urgency_hint: str | None = None

    certainty_hint: str | None = None

    source_url: str | None = None

    geometry_geojson: dict[str, Any] | None = None

    published_at: datetime | None = None
