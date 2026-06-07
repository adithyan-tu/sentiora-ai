from __future__ import annotations

import feedparser

from app.ingestion.schemas.gdacs import GDACSEvent

GDACS_RSS_URL = "https://www.gdacs.org/xml/rss.xml"


class GDACSAdapter:
    """
    GDACS RSS ingestion adapter.
    """

    async def fetch_events(
        self,
    ) -> list[GDACSEvent]:
        feed = feedparser.parse(
            GDACS_RSS_URL,
        )

        events: list[GDACSEvent] = []

        for entry in feed.entries:
            latitude = None
            longitude = None

            geo_point = entry.get("geo_point")

            if geo_point:
                latitude = float(geo_point.get("lat"))
                longitude = float(geo_point.get("long"))

            event = GDACSEvent(
                event_id=entry.get("id", entry.link),
                title=entry.title,
                link=entry.link,
                summary=entry.get("summary"),
                category=entry.get("gdacs_eventtype"),
                alert_level=entry.get("gdacs_alertlevel"),
                published_at=entry.get("published"),
                latitude=latitude,
                longitude=longitude,
            )

            events.append(event)

        return events
