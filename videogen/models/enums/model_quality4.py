from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality4(str, Enum):
    """Image generation quality tier for AI-generated visuals. Optional; when omitted, your account's Default AI quality
    for images is used (change it at https://app.videogen.io/settings/account). Only applies when ``visualStyle.type``
    is AI_IMAGE; STOCK pulls existing footage and is unaffected."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality4OrStr: TypeAlias = Annotated[ModelQuality4 | str, open_enum_validator(ModelQuality4)]
