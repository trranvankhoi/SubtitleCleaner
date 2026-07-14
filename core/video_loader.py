from pathlib import Path
from typing import Any

from utils.logger import logger
from core.metadata import VideoMetadata


class VideoLoader:
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> VideoMetadata:
        logger.debug("Loading video metadata: %s", self.path)
        if not self.path.exists():
            raise FileNotFoundError(f"Video file not found: {self.path}")
        return VideoMetadata.from_path(self.path)
