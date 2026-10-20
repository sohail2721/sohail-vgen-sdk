from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WatermarkMode(str, Enum):
    """Controls whether the VideoGen watermark is applied to the output. ``AUTO`` applies the watermark unless you have
    a Pro plan. ``VIDEO_GEN`` always applies it. ``NONE`` removes the watermark (requires Pro; returns an error if you
    don't have it)."""

    NONE = "NONE"
    VIDEO_GEN = "VIDEO_GEN"
    AUTO = "AUTO"

    __str__ = str.__str__


WatermarkModeOrStr: TypeAlias = Annotated[WatermarkMode | str, open_enum_validator(WatermarkMode)]
