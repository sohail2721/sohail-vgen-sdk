from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality2(str, Enum):
    """Image generation quality tier for the restyled images. Optional; when omitted, your account's Default AI quality
    for images is used (change it at https://app.videogen.io/settings/account)."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality2OrStr: TypeAlias = Annotated[ModelQuality2 | str, open_enum_validator(ModelQuality2)]
