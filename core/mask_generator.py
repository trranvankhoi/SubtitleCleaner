from pathlib import Path
from typing import List, Tuple

import numpy as np
from PIL import Image

from utils.logger import logger


class MaskGenerator:
    def __init__(self, expansion: int = 8, blur_radius: int = 5) -> None:
        self.expansion = expansion
        self.blur_radius = blur_radius

    def generate(self, frame_path: Path, regions: List[Tuple[int, int, int, int]]) -> Image.Image:
        logger.debug("Generating mask for %s with regions %s", frame_path, regions)
        width, height = 1920, 1080
        mask_image = Image.new("L", (width, height), 0)
        return mask_image
