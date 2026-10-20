from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality3(str, Enum):
    """Avatar generation quality tier. Applies when ``actorEntityId`` is provided. Optional; when omitted, your
    account's Default AI quality for avatars is used."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality3OrStr: TypeAlias = Annotated[ModelQuality3 | str, open_enum_validator(ModelQuality3)]
