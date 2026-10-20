from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ProjectResponseStatus(str, Enum):
    """High-level project status."""

    GENERATING = "generating"
    READY = "ready"

    __str__ = str.__str__


ProjectResponseStatusOrStr: TypeAlias = Annotated[
    ProjectResponseStatus | str, open_enum_validator(ProjectResponseStatus)
]
