import sys
import logging

import structlog

from app.core.config import get_settings
from app.core.log_context import get_request_id


settings = get_settings()


def add_request_id(_, __, event_dict):
    event_dict["request_id"] = get_request_id()
    return event_dict

def configure_logging():
    timestamper = structlog.processors.TimeStamper(fmt="iso")

    processors = [
        add_request_id,
        structlog.processors.add_log_level,
        timestamper,
    ]

    if settings.ENV == "dev":
        processors.append(structlog.dev.ConsoleRenderer())
    else:
        processors.append(structlog.processors.JSONRenderer())
    
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.INFO
        ),
        logger_factory=structlog.PrintLoggerFactory(file=sys.stdout),
        cache_logger_on_first_use=True,
    )