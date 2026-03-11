import os
import sys
from logging.config import dictConfig

# Log directory and file name
# ./app/logs/system.log
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")

os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "system.log")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": sys.stdout,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": LOG_FILE,
            "maxBytes": 5_000_000,
            "backupCount": 5,
        },
    },

    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
    "loggers": {
        "sqlalchemy.engine": {
            "level": "WARNING",
            "handlers": ["console", "file"],
            "propagate": False,
        },
    },
}

def setup_logging():
    dictConfig(LOGGING_CONFIG)
