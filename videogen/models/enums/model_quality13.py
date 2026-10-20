from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality13(str, Enum):
    """Text generation quality tier. Optional; when omitted, your account's Default AI quality for text is used (change
    it at https://app.videogen.io/settings/account)."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality13OrStr: TypeAlias = Annotated[ModelQuality13 | str, open_enum_validator(ModelQuality13)]
