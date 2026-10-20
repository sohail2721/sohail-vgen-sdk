from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AspectRatio4(SdkBaseModel):
    """Aspect ratio for the generated motion graphic. Defaults to 16:9 when omitted."""

    width: int
    height: int


class AspectRatio4Dict(TypedDict):
    width: int
    height: int
