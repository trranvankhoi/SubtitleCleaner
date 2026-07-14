from pathlib import Path
from typing import List

from utils.logger import logger


class FrameExtractor:
    def __init__(self, video_path: Path, output_dir: Path) -> None:
        self.video_path = video_path
        self.output_dir = output_dir

    def extract_frames(self) -> List[Path]:
        logger.debug("Extracting frames from %s", self.video_path)
        return []
