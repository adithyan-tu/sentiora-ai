from __future__ import annotations

from app.ingestion.normalizers.noaa import NOAANormalizer
from app.ingestion.schemas.noaa import NOAAAlertFeature


def test_noaa_normalization() -> None:
    payload = NOAAAlertFeature.model_validate(
        {
            "id": "abc123",
            "geometry": {
                "type": "Polygon",
            },
            "properties": {
                "event": "Flood Warning",
                "headline": "Major Flood Warning",
                "description": "Flooding expected.",
                "severity": "Severe",
                "urgency": "Immediate",
                "certainty": "Likely",
                "sent": "2025-06-01T10:00:00+00:00",
            },
        }
    )

    normalizer = NOAANormalizer()

    event = normalizer.normalize(payload)

    assert event.source_name == "NOAA"

    assert event.source_event_id == "abc123"

    assert event.title == "Major Flood Warning"

    assert event.category == "Flood Warning"

    assert event.severity_hint == "Severe"
