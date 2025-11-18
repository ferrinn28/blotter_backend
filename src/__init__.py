from .app import app

import logging, logging.config
from dotenv import load_dotenv


load_dotenv()

LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",  # Added date format
        }
    },
    "handlers": {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "INFO",
        }
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {"propagate": True},
        "uvicorn.error": {"propagate": True},
    },
}


logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)