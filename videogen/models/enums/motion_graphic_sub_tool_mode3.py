from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MotionGraphicSubToolMode3(str, Enum):
    """Whether the motion graphic may generate voiceover audio. Defaults to AUTO."""

    AUTO = "AUTO"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    __str__ = str.__str__


MotionGraphicSubToolMode3OrStr: TypeAlias = Annotated[
    MotionGraphicSubToolMode3 | str, open_enum_validator(MotionGraphicSubToolMode3)
]
