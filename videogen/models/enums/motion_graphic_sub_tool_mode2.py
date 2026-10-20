from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MotionGraphicSubToolMode2(str, Enum):
    """Whether the motion graphic may generate video clips. Requires a paid plan. Defaults to AUTO."""

    AUTO = "AUTO"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    __str__ = str.__str__


MotionGraphicSubToolMode2OrStr: TypeAlias = Annotated[
    MotionGraphicSubToolMode2 | str, open_enum_validator(MotionGraphicSubToolMode2)
]
