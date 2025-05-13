import os
from typing import Final

from loguru import logger
from rich.logging import RichHandler

LOGURU_LEVEL: Final[str] = os.getenv("LOGURU_LEVEL", "INFO")
logger.configure(
    handlers=[
        {
            "sink": RichHandler(show_time=False, omit_repeated_times=False, show_level=False, show_path=False),
            "level": LOGURU_LEVEL,
            # "format": "{time:YYYY-MM-DD HH:mm:ss,SSS} {level: <8} '{name}:{function}:{line}' {message}",
        },
    ]
)
