from __future__ import annotations

from dateutil.parser import isoparse

from app.ingestion.schemas.noaa import NOAAAlertFeature
from app.ingestion.schemas.normalized_event import NormalizedEvent


class NOAANormalizer:
    """
    Converts NOAA alerts into canonical normalized events.
    """

    def normalize(
        self,
        alert: NOAAAlertFeature,
    ) -> NormalizedEvent:
        properties = alert.properties

        return NormalizedEvent(
            source_name="NOAA",
            source_event_id=alert.id,
            title=properties.headline or properties.event or "NOAA Alert",
            summary=properties.description,
            category=properties.event,
            severity_hint=properties.severity,
            urgency_hint=properties.urgency,
            certainty_hint=properties.certainty,
            source_url=properties.id,
            geometry_geojson=alert.geometry,
            published_at=isoparse(properties.sent) if properties.sent else None,
        )
