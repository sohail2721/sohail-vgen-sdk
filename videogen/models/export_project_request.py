from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.end_screen_mode import EndScreenMode, EndScreenModeOrStr
from .enums.export_project_quality import ExportProjectQualityOrStr
from .enums.watermark_mode import WatermarkMode, WatermarkModeOrStr
from .export_delivery_destination import ExportDeliveryDestination, ExportDeliveryDestinationDict


class ExportProjectRequest(SdkBaseModel):
    quality: Optional[ExportProjectQualityOrStr] = UNSET
    """Vertical resolution tier for the rendered MP4."""

    watermark_mode: WatermarkModeOrStr = Field(default=WatermarkMode.AUTO, alias="watermarkMode")
    """Controls whether the VideoGen watermark is applied to the output. ``AUTO`` applies the watermark unless you have
    a Pro plan. ``VIDEO_GEN`` always applies it. ``NONE`` removes the watermark (requires Pro; returns an error if you
    don't have it)."""

    end_screen_mode: EndScreenModeOrStr = Field(default=EndScreenMode.AUTO, alias="endScreenMode")
    """Controls whether a short 'Made with VideoGen' end screen is appended to the output. ``AUTO`` appends it unless
    you have a Pro plan. ``VIDEO_GEN`` always appends it. ``NONE`` removes it (requires Pro; returns an error if you
    don't have it)."""

    delivery_destinations: Optional[list[ExportDeliveryDestination]] = Field(
        default=UNSET, alias="deliveryDestinations"
    )
    """Destinations to deliver the finished export to when it completes, in addition to any delivery destinations
    already saved for the team. Each destination references a connected integration."""


class ExportProjectRequestDict(TypedDict):
    quality: NotRequired[ExportProjectQualityOrStr]
    watermark_mode: NotRequired[WatermarkModeOrStr]
    end_screen_mode: NotRequired[EndScreenModeOrStr]
    delivery_destinations: NotRequired[list[ExportDeliveryDestinationDict]]
