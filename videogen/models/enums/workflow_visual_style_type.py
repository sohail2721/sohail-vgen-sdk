from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkflowVisualStyleType(str, Enum):
    """STOCK pulls stock footage and images. AI_IMAGE generates a styled image for each section. Pass ``entityId`` to
    match a saved visual-style entity, or ``aiStyle`` for a free-form look."""

    STOCK = "STOCK"
    AI_IMAGE = "AI_IMAGE"

    __str__ = str.__str__


WorkflowVisualStyleTypeOrStr: TypeAlias = Annotated[
    WorkflowVisualStyleType | str, open_enum_validator(WorkflowVisualStyleType)
]
