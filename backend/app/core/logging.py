import logging
import sys

from pythonjsonlogger.json import JsonFormatter

from app.core.config import settings


def setup_logging() -> None:
    log_handler = logging.StreamHandler(sys.stdout)

    formatter = JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )

    log_handler.setFormatter(formatter)

    logging.basicConfig(
        level=settings.LOG_LEVEL,
        handlers=[log_handler],
    )