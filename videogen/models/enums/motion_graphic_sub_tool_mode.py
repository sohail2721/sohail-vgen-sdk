from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class MotionGraphicSubToolMode(str, Enum):
    """Access mode for a motion graphic capability. AUTO uses the capability only when it is available on your plan
    (generated video clips require a paid plan). ENABLED forces the capability on and returns an upgrade error if your
    plan lacks it. DISABLED prevents the motion graphic from using the capability."""

    AUTO = "AUTO"
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"

    __str__ = str.__str__


MotionGraphicSubToolModeOrStr: TypeAlias = Annotated[
    MotionGraphicSubToolMode | str, open_enum_validator(MotionGraphicSubToolMode)
]
