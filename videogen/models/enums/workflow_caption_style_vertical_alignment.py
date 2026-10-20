from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkflowCaptionStyleVerticalAlignment(str, Enum):
    """Vertical position of the caption block in the frame."""

    TOP = "TOP"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"

    __str__ = str.__str__


WorkflowCaptionStyleVerticalAlignmentOrStr: TypeAlias = Annotated[
    WorkflowCaptionStyleVerticalAlignment | str, open_enum_validator(WorkflowCaptionStyleVerticalAlignment)
]
