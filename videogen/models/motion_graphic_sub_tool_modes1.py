from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.motion_graphic_sub_tool_mode1 import MotionGraphicSubToolMode1OrStr
from .enums.motion_graphic_sub_tool_mode2 import MotionGraphicSubToolMode2OrStr
from .enums.motion_graphic_sub_tool_mode3 import MotionGraphicSubToolMode3OrStr
from .enums.motion_graphic_sub_tool_mode4 import MotionGraphicSubToolMode4OrStr


class MotionGraphicSubToolModes1(SdkBaseModel):
    """Optional per-capability controls for the media the motion graphic may generate or fetch (generated images,
    generated video clips, generated voiceover, and stock media search). Each capability is AUTO, ENABLED, or DISABLED.
    Omit to use AUTO for every capability."""

    generate_images: Optional[MotionGraphicSubToolMode1OrStr] = Field(default=UNSET, alias="generateImages")
    """Whether the motion graphic may generate images. Defaults to AUTO."""

    generate_video_clips: Optional[MotionGraphicSubToolMode2OrStr] = Field(default=UNSET, alias="generateVideoClips")
    """Whether the motion graphic may generate video clips. Requires a paid plan. Defaults to AUTO."""

    generate_voiceover: Optional[MotionGraphicSubToolMode3OrStr] = Field(default=UNSET, alias="generateVoiceover")
    """Whether the motion graphic may generate voiceover audio. Defaults to AUTO."""

    search_stock_media: Optional[MotionGraphicSubToolMode4OrStr] = Field(default=UNSET, alias="searchStockMedia")
    """Whether the motion graphic may search stock media. Defaults to AUTO."""


class MotionGraphicSubToolModes1Dict(TypedDict):
    generate_images: NotRequired[MotionGraphicSubToolMode1OrStr]
    generate_video_clips: NotRequired[MotionGraphicSubToolMode2OrStr]
    generate_voiceover: NotRequired[MotionGraphicSubToolMode3OrStr]
    search_stock_media: NotRequired[MotionGraphicSubToolMode4OrStr]
