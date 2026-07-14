from pathlib import Path
from typing import Tuple

from PIL import Image

from utils.logger import logger


class MaskRefiner:
    def __init__(self, expansion: int = 8, blur_radius: int = 5) -> None:
        self.expansion = expansion
        self.blur_radius = blur_radius

    def refine(self, mask: Image.Image) -> Image.Image:
        logger.debug("Refining mask with expansion=%s blur_radius=%s", self.expansion, self.blur_radius)
        return mask
