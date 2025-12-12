"""Project Template Generator - Create structured project templates."""

__version__ = "1.0.0"
__author__ = "Leila"

from .generator import ProjectGenerator
from .templates import TEMPLATES

__all__ = ["ProjectGenerator", "TEMPLATES"]