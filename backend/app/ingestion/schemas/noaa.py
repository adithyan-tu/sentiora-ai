from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class NOAAAlertProperties(BaseModel):
    id: str | None = None
    areaDesc: str | None = None
    severity: str | None = None
    urgency: str | None = None
    certainty: str | None = None
    event: str | None = None
    headline: str | None = None
    description: str | None = None


class NOAAAlertFeature(BaseModel):
    id: str
    properties: NOAAAlertProperties
    geometry: dict[str, Any] | None = None


class NOAAAlertsResponse(BaseModel):
    features: list[NOAAAlertFeature]
