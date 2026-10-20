from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.watermark_mode import WatermarkMode, WatermarkModeOrStr


class VideoAssetRequest(SdkBaseModel):
    video_file_id: str = Field(alias="videoFileId")
    """File id of the source video (e.g. ``vg_file_...``). Upload a file first via ``POST /v1/files/upload``, then pass
    the returned id here."""

    watermark_mode: WatermarkModeOrStr = Field(default=WatermarkMode.AUTO, alias="watermarkMode")
    """Controls whether the VideoGen watermark is applied to the output. ``AUTO`` applies the watermark unless you have
    a Pro plan. ``VIDEO_GEN`` always applies it. ``NONE`` removes the watermark (requires Pro; returns an error if you
    don't have it)."""

    num_results: int = Field(default=1, alias="numResults")
    """Number of output results to generate. Defaults to 1."""

    is_output_temporary: bool = Field(default=False, alias="isOutputTemporary")
    """When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after
    which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding
    will be generated), so they will not appear in search results. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, generated files are hidden from the VideoGen Media page by default. They remain accessible through the
    API. Defaults to false."""


class VideoAssetRequestDict(TypedDict):
    video_file_id: str
    watermark_mode: NotRequired[WatermarkModeOrStr]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
