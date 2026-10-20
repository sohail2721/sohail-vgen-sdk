from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SceneDescriptionRange(SdkBaseModel):
    """A description of the visuals to show during an absolute time range of the finished video."""

    start_seconds: float = Field(alias="startSeconds")
    """Start time of the range in seconds from the beginning of the video."""

    end_seconds: float = Field(alias="endSeconds")
    """End time of the range in seconds from the beginning of the video. Must be greater than ``startSeconds``."""

    description: str
    """What should be shown on screen during this range (e.g. the b-roll subject, on-screen text, or staging)."""


class SceneDescriptionRangeDict(TypedDict):
    start_seconds: float
    end_seconds: float
    description: str
