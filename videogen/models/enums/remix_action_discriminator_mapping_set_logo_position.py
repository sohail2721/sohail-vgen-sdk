from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RemixActionDiscriminatorMappingSetLogoPosition(str, Enum):
    """Position the logo is anchored to. Omit or pass ``null`` to keep the current position."""

    TOP_LEFT = "TOP_LEFT"
    TOP_CENTER = "TOP_CENTER"
    TOP_RIGHT = "TOP_RIGHT"
    BOTTOM_LEFT = "BOTTOM_LEFT"
    BOTTOM_CENTER = "BOTTOM_CENTER"
    BOTTOM_RIGHT = "BOTTOM_RIGHT"

    __str__ = str.__str__


RemixActionDiscriminatorMappingSetLogoPositionOrStr: TypeAlias = Annotated[
    RemixActionDiscriminatorMappingSetLogoPosition | str,
    open_enum_validator(RemixActionDiscriminatorMappingSetLogoPosition),
]
