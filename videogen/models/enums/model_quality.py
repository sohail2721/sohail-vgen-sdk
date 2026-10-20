from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ModelQuality(str, Enum):
    """AI generation quality tier, shared across every generative feature (image, video, text, and so on). ``LOW`` is
    fastest and cheapest, ``STANDARD`` balances quality and cost, ``HIGH`` is higher quality, and ``MAX`` is the highest
    quality.

    When a request omits the quality field, VideoGen falls back to your account's **Default AI quality** for that
    feature, which you can change at `Account settings <https://app.videogen.io/settings/account>`__. Not every feature
    supports every tier; unsupported tiers are rejected with an error (see each field's description)."""

    LOW = "LOW"
    STANDARD = "STANDARD"
    HIGH = "HIGH"
    MAX = "MAX"

    __str__ = str.__str__


ModelQualityOrStr: TypeAlias = Annotated[ModelQuality | str, open_enum_validator(ModelQuality)]
