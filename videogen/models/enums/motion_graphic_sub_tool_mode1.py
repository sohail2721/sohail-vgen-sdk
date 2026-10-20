from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MotionGraphicSubToolMode1(str, Enum):
    """Whether the motion graphic may generate images. Defaults to AUTO."""

    AUTO = "AUTO"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    __str__ = str.__str__


MotionGraphicSubToolMode1OrStr: TypeAlias = Annotated[
    MotionGraphicSubToolMode1 | str, open_enum_validator(MotionGraphicSubToolMode1)
]
