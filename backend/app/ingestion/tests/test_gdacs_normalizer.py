from __future__ import annotations

from app.ingestion.normalizers.gdacs import (
    GDACSNormalizer,
)
from app.ingestion.schemas.gdacs import GDACSEvent


def test_gdacs_normalization() -> None:
    event = GDACSEvent(
        event_id="gdacs123",
        title="Major Earthquake",
        link="https://example.com",
        summary="Earthquake detected",
        category="EQ",
        alert_level="Red",
        published_at="2026-06-06T10:00:00Z",
        latitude=10.0,
        longitude=20.0,
    )

    normalizer = GDACSNormalizer()

    normalized = normalizer.normalize(
        event,
    )

    assert normalized.source_name == "GDACS"

    assert normalized.category == "EQ"

    assert normalized.severity_hint == "Red"

    assert normalized.geometry_geojson["type"] == "Point"
