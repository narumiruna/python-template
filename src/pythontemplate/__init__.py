import os
import sys
from typing import Final

from loguru import logger

LOGURU_LEVEL: Final[str] = os.getenv("LOGURU_LEVEL", "INFO")
logger.remove()
logger.add(sys.stderr, level=LOGURU_LEVEL)
