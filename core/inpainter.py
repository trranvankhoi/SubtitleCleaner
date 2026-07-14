from abc import ABC, abstractmethod
from pathlib import Path
from typing import List

import numpy as np
from PIL import Image

from utils.logger import logger


class BaseInpainter(ABC):
    @abstractmethod
    def inpaint(self, image: Image.Image, mask: Image.Image) -> Image.Image:
        raise NotImplementedError


class OpenCVTeleaInpainter(BaseInpainter):
    def inpaint(self, image: Image.Image, mask: Image.Image) -> Image.Image:
        import cv2

        logger.debug("Running OpenCV Telea inpainter")
        source = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        mask_array = np.array(mask)
        inpainted = cv2.inpaint(source, mask_array, 3, cv2.INPAINT_TELEA)
        return Image.fromarray(cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB))


class OpenCVNavierStokesInpainter(BaseInpainter):
    def inpaint(self, image: Image.Image, mask: Image.Image) -> Image.Image:
        import cv2

        logger.debug("Running OpenCV Navier-Stokes inpainter")
        source = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        mask_array = np.array(mask)
        inpainted = cv2.inpaint(source, mask_array, 3, cv2.INPAINT_NS)
        return Image.fromarray(cv2.cvtColor(inpainted, cv2.COLOR_BGR2RGB))


class InpainterFactory:
    @staticmethod
    def create(mode: str) -> BaseInpainter:
        if mode == "fast":
            return OpenCVTeleaInpainter()
        if mode == "compatibility":
            return OpenCVNavierStokesInpainter()
        raise ValueError(f"Unsupported inpainter mode: {mode}")
