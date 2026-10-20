from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CreateEntityRequestEntityType(str, Enum):
    """ACTOR features a consistent character; PRODUCT features a consistent product or object; VISUAL_STYLE guides the
    look of generated images; SLIDESHOW_THEME is a shared slide design system (fonts, colors, layout) applied to every
    slide of a slideshow-to-video deck."""

    ACTOR = "ACTOR"
    PRODUCT = "PRODUCT"
    VISUAL_STYLE = "VISUAL_STYLE"
    SLIDESHOW_THEME = "SLIDESHOW_THEME"

    __str__ = str.__str__


CreateEntityRequestEntityTypeOrStr: TypeAlias = Annotated[
    CreateEntityRequestEntityType | str, open_enum_validator(CreateEntityRequestEntityType)
]
