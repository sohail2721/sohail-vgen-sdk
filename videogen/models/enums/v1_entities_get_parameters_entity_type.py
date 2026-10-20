from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class V1EntitiesGetParametersEntityType(str, Enum):
    ACTOR = "ACTOR"
    PRODUCT = "PRODUCT"
    VISUAL_STYLE = "VISUAL_STYLE"
    SLIDESHOW_THEME = "SLIDESHOW_THEME"

    __str__ = str.__str__


V1EntitiesGetParametersEntityTypeOrStr: TypeAlias = Annotated[
    V1EntitiesGetParametersEntityType | str, open_enum_validator(V1EntitiesGetParametersEntityType)
]
