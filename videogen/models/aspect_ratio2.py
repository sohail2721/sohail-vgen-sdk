from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AspectRatio2(SdkBaseModel):
    """Aspect ratio for the generated image. Defaults to 16:9 when omitted."""

    width: int
    height: int


class AspectRatio2Dict(TypedDict):
    width: int
    height: int
