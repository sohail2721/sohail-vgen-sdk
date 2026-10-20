from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.model_quality12 import ModelQuality12OrStr
from .enums.watermark_mode import WatermarkMode, WatermarkModeOrStr


class GenerateAvatarRequest(SdkBaseModel):
    """Generate a talking-head avatar from an ACTOR entity and audio."""

    actor_entity_id: str = Field(alias="actorEntityId")
    """The id of a built-in stock actor or an ACTOR entity (e.g. ``vg_enti_...``) with an image reference."""

    avatar_quality: Optional[ModelQuality12OrStr] = Field(default=UNSET, alias="avatarQuality")
    """Avatar generation quality tier. Optional; when omitted, your account's Default AI quality for avatars is used."""

    audio_file_id: str = Field(alias="audioFileId")
    """File id of an AUDIO file (e.g. ``vg_file_...``), typically from a prior text-to-speech result. Upload a file
    first via ``POST /v1/files/upload`` or generate one with ``POST /v1/tools/text-to-speech``, then pass the returned
    id here."""

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


class GenerateAvatarRequestDict(TypedDict):
    actor_entity_id: str
    avatar_quality: NotRequired[ModelQuality12OrStr]
    audio_file_id: str
    watermark_mode: NotRequired[WatermarkModeOrStr]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
