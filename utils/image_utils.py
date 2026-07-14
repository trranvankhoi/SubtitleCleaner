from pathlib import Path
from typing import Tuple

import numpy as np
from PIL import Image


def load_image(path: Path) -> Image.Image:
    return Image.open(path).convert("RGB")


def save_image(image: Image.Image, path: Path) -> None:
    image.save(path)


def resize_image(image: Image.Image, size: Tuple[int, int]) -> Image.Image:
    return image.resize(size)


def image_to_array(image: Image.Image) -> np.ndarray:
    return np.array(image)


def array_to_image(array: np.ndarray) -> Image.Image:
    return Image.fromarray(array)
