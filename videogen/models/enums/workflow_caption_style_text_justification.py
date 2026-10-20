from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkflowCaptionStyleTextJustification(str, Enum):
    LEFT = "LEFT"
    CENTER = "CENTER"
    RIGHT = "RIGHT"

    __str__ = str.__str__


WorkflowCaptionStyleTextJustificationOrStr: TypeAlias = Annotated[
    WorkflowCaptionStyleTextJustification | str, open_enum_validator(WorkflowCaptionStyleTextJustification)
]
