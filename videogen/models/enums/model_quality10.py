from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality10(str, Enum):
    """Image generation quality tier. Optional; when omitted, your account's Default AI quality for images is used
    (change it at https://app.videogen.io/settings/account)."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality10OrStr: TypeAlias = Annotated[ModelQuality10 | str, open_enum_validator(ModelQuality10)]
