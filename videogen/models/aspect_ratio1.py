from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AspectRatio1(SdkBaseModel):
    """Aspect ratio for the generated video. Defaults to 16:9 when omitted."""

    width: int
    height: int


class AspectRatio1Dict(TypedDict):
    width: int
    height: int
