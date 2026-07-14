from pathlib import Path
from typing import Optional

from utils.logger import logger


class VideoWriter:
    def __init__(self, output_path: Path, codec: str = "libx264", crf: int = 18, bitrate: Optional[str] = None) -> None:
        self.output_path = output_path
        self.codec = codec
        self.crf = crf
        self.bitrate = bitrate

    def write(self, frames_directory: Path, source_video: Path) -> Path:
        logger.debug("Writing output video to %s", self.output_path)
        return self.output_path
