"""Foundation package for the pecan vision workshop."""

from .config import WorkshopConfig, load_config
from .model import BaseVisionModel

__all__ = ["BaseVisionModel", "WorkshopConfig", "load_config"]
__version__ = "0.1.0"
