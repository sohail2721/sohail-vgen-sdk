from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class AspectRatio(SdkBaseModel):
    """Aspect ratio as a width:height pair (e.g. 16 and 9 for 16:9). Not pixel dimensions."""

    width: int
    height: int


class AspectRatioDict(TypedDict):
    width: int
    height: int
