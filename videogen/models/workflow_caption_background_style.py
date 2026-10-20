from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.workflow_caption_background_style_type import WorkflowCaptionBackgroundStyleTypeOrStr
from .workflow_rgb_color import WorkflowRgbColor, WorkflowRgbColorDict


class WorkflowCaptionBackgroundStyle(SdkBaseModel):
    """Background drawn behind caption text."""

    type_: WorkflowCaptionBackgroundStyleTypeOrStr = Field(alias="type")
    """RECT draws one rectangle behind the whole line; WRAPPED hugs the text; WORD_BY_WORD draws a box per word."""

    background_color: WorkflowRgbColor = Field(alias="backgroundColor")
    """An RGB color. Each channel is an integer from 0 to 255."""

    border_radius_proportion: Optional[float] = Field(default=UNSET, alias="borderRadiusProportion")
    """Corner rounding as a proportion of the background height, between 0 (square corners) and 1 (fully rounded)."""

    opacity_proportion: Optional[float] = Field(default=UNSET, alias="opacityProportion")
    """Background opacity from 0 (transparent) to 1 (opaque)."""


class WorkflowCaptionBackgroundStyleDict(TypedDict):
    type_: WorkflowCaptionBackgroundStyleTypeOrStr
    background_color: WorkflowRgbColorDict
    border_radius_proportion: NotRequired[float]
    opacity_proportion: NotRequired[float]
