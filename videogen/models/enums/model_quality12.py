from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality12(str, Enum):
    """Avatar generation quality tier. Optional; when omitted, your account's Default AI quality for avatars is used."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality12OrStr: TypeAlias = Annotated[ModelQuality12 | str, open_enum_validator(ModelQuality12)]
