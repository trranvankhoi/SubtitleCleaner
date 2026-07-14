from enum import Enum
from pathlib import Path
from typing import List, Tuple

from utils.logger import logger


class DetectionMode(str, Enum):
    MANUAL = "manual"
    AUTO = "auto"


class SubtitleDetector:
    def __init__(self, mode: DetectionMode = DetectionMode.MANUAL) -> None:
        self.mode = mode

    def detect(self, frame_path: Path) -> List[Tuple[int, int, int, int]]:
        logger.debug("Detecting subtitles in %s using mode %s", frame_path, self.mode)
        return []
