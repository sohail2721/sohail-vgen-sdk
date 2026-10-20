from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MotionGraphicSubToolMode4(str, Enum):
    """Whether the motion graphic may search stock media. Defaults to AUTO."""

    AUTO = "AUTO"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    __str__ = str.__str__


MotionGraphicSubToolMode4OrStr: TypeAlias = Annotated[
    MotionGraphicSubToolMode4 | str, open_enum_validator(MotionGraphicSubToolMode4)
]
