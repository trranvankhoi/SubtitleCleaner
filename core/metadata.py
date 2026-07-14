from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any

from utils.logger import logger
from core.ffmpeg_wrapper import FFmpegWrapper


@dataclass
class VideoMetadata:
    width: int
    height: int
    fps: float
    duration: float
    codec: str
    format_name: str
    streams: Dict[str, Any]

    @classmethod
    def from_path(cls, path: Path) -> "VideoMetadata":
        probe = FFmpegWrapper.probe(path)
        format_info = probe.get("format", {})
        video_stream = next((stream for stream in probe.get("streams", []) if stream.get("codec_type") == "video"), None)
        if video_stream is None:
            raise ValueError("No video stream found")
        width = int(video_stream.get("width", 0))
        height = int(video_stream.get("height", 0))
        fps = cls._parse_fps(video_stream.get("r_frame_rate", "0/1"))
        duration = float(format_info.get("duration", 0.0))
        codec = video_stream.get("codec_name", "unknown")
        return cls(
            width=width,
            height=height,
            fps=fps,
            duration=duration,
            codec=codec,
            format_name=format_info.get("format_name", "unknown"),
            streams=video_stream,
        )

    @staticmethod
    def _parse_fps(r_frame_rate: str) -> float:
        numerator, denominator = r_frame_rate.split("/")
        return float(numerator) / float(denominator) if int(denominator) != 0 else 0.0
