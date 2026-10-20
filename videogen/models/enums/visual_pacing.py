from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class VisualPacing(str, Enum):
    """How quickly visuals change. FAST shows more, shorter shots; SLOW holds each visual longer. Defaults to MEDIUM."""

    FAST = "FAST"
    MEDIUM = "MEDIUM"
    SLOW = "SLOW"

    __str__ = str.__str__


VisualPacingOrStr: TypeAlias = Annotated[VisualPacing | str, open_enum_validator(VisualPacing)]
