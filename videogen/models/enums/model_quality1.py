from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality1(str, Enum):
    """Video generation quality tier for the image-to-video conversions (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``).
    Optional; when omitted, your account's Default AI quality for video is used (change it at
    https://app.videogen.io/settings/account)."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQuality1OrStr: TypeAlias = Annotated[ModelQuality1 | str, open_enum_validator(ModelQuality1)]
