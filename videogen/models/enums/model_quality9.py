from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality9(str, Enum):
    """Video generation quality tier (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Also used for the opening-frame
    image. Optional; when omitted, your account's Default AI quality for video is used (change it at
    https://app.videogen.io/settings/account)."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality9OrStr: TypeAlias = Annotated[ModelQuality9 | str, open_enum_validator(ModelQuality9)]
