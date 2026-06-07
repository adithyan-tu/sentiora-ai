from __future__ import annotations

from dateutil.parser import parse

from app.ingestion.schemas.gdacs import GDACSEvent
from app.ingestion.schemas.normalized_event import NormalizedEvent


class GDACSNormalizer:
    """
    Converts GDACS events into canonical events.
    """

    def normalize(
        self,
        event: GDACSEvent,
    ) -> NormalizedEvent:
        geometry = None

        if event.latitude is not None and event.longitude is not None:
            geometry = {
                "type": "Point",
                "coordinates": [
                    event.longitude,
                    event.latitude,
                ],
            }

        return NormalizedEvent(
            source_name="GDACS",
            source_event_id=event.event_id,
            title=event.title,
            summary=event.summary,
            category=event.category,
            severity_hint=event.alert_level,
            urgency_hint=None,
            certainty_hint=None,
            source_url=event.link,
            geometry_geojson=geometry,
            published_at=parse(event.published_at) if event.published_at else None,
        )
