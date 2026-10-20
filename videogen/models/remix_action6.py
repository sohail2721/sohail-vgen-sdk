from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .aspect_ratio import AspectRatio, AspectRatioDict


class RemixAction6(SdkBaseModel):
    """Change the project's output aspect ratio (e.g. to a vertical 9:16 social format). The video is re-flowed to the
    new ratio."""

    type_: Literal["RESIZE_PROJECT"] = Field(default="RESIZE_PROJECT", alias="type")
    """Discriminator value: RESIZE_PROJECT"""

    aspect_ratio: AspectRatio = Field(alias="aspectRatio")
    """Aspect ratio as a width:height pair (e.g. 16 and 9 for 16:9). Not pixel dimensions."""


class RemixAction6Dict(TypedDict):
    type_: Literal["RESIZE_PROJECT"]
    aspect_ratio: AspectRatioDict
