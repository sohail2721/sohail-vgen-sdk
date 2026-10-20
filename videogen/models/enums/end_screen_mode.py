from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class EndScreenMode(str, Enum):
    """Controls whether a short 'Made with VideoGen' end screen is appended to the output. ``AUTO`` appends it unless
    you have a Pro plan. ``VIDEO_GEN`` always appends it. ``NONE`` removes it (requires Pro; returns an error if you
    don't have it)."""

    NONE = "NONE"
    VIDEO_GEN = "VIDEO_GEN"
    AUTO = "AUTO"

    __str__ = str.__str__


EndScreenModeOrStr: TypeAlias = Annotated[EndScreenMode | str, open_enum_validator(EndScreenMode)]
