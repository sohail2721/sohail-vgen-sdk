from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WorkflowRgbColor(SdkBaseModel):
    """An RGB color. Each channel is an integer from 0 to 255."""

    red: int
    green: int
    blue: int


class WorkflowRgbColorDict(TypedDict):
    red: int
    green: int
    blue: int
