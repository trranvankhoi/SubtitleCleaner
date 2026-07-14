from pathlib import Path
from typing import Dict, Optional

import ffmpeg

from utils.logger import logger


class FFmpegWrapper:
    @staticmethod
    def probe(path: Path) -> Dict[str, any]:
        logger.debug("Probing video file %s", path)
        return ffmpeg.probe(str(path))

    @staticmethod
    def extract_audio(input_path: Path, output_path: Path) -> None:
        logger.debug("Extracting audio from %s to %s", input_path, output_path)
        (ffmpeg.input(str(input_path)).output(str(output_path), vn=None, acodec="copy").overwrite_output().run(capture_stdout=True, capture_stderr=True))

    @staticmethod
    def encode_video(frames_dir: Path, output_path: Path, codec: str, crf: int, bitrate: Optional[str], fps: int) -> None:
        logger.debug("Encoding video to %s using codec=%s crf=%s bitrate=%s", output_path, codec, crf, bitrate)
        raise NotImplementedError
