from dataclasses import dataclass
from pathlib import Path


@dataclass
class AppConfig:
    output_folder: Path
    temp_folder: Path
    inpainter_mode: str = "high_quality"
    expansion: int = 8
    blur_radius: int = 5
    codec: str = "libx264"
    crf: int = 18
    bitrate: str = ""
    threads: int = 4
    gpu_enabled: bool = True


DEFAULT_CONFIG = AppConfig(
    output_folder=Path.cwd() / "output",
    temp_folder=Path.cwd() / "temp",
)
