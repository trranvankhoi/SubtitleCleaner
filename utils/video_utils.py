from pathlib import Path
from typing import Optional

from core.metadata import VideoMetadata
from core.ffmpeg_wrapper import FFmpegWrapper


def load_metadata(video_path: Path) -> VideoMetadata:
    return VideoMetadata.from_path(video_path)


def get_video_codec(video_path: Path) -> Optional[str]:
    metadata = load_metadata(video_path)
    return metadata.codec
