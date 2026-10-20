from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .aspect_ratio1 import AspectRatio1, AspectRatio1Dict
from .content_policy_config import ContentPolicyConfig, ContentPolicyConfigDict
from .enums.model_quality11 import ModelQuality11OrStr
from .enums.watermark_mode import WatermarkMode, WatermarkModeOrStr


class GenerateVideoClipRequest(SdkBaseModel):
    """At least one of ``prompt``, ``startFrameFileId``, ``imageFileIds``, ``videoFileIds``, ``audioFileIds``, or
    ``spokenDialogue`` must be provided."""

    prompt: Optional[str] = UNSET
    """Text prompt describing the video to generate. Optional when reference media, ``startFrameFileId``, or
    ``spokenDialogue`` is provided. Describe the video in plain language; any reference media you provide is
    incorporated automatically."""

    start_frame_file_id: Optional[str] = Field(default=UNSET, alias="startFrameFileId")
    """Optional file id of the opening-frame still (e.g. ``vg_file_...``). Upload first via ``POST /v1/files/upload``.
    When set, this image is the first frame of the clip. If the same id also appears in ``imageFileIds``, it is used
    only as the opening frame and dropped from the reference list. Can be the only input (prompt optional)."""

    image_file_ids: Optional[list[str]] = Field(default=UNSET, alias="imageFileIds")
    """Optional file ids of reference images (e.g. ``["vg_file_..."]``). Upload files first via ``POST
    /v1/files/upload``, then pass the returned ids here. When provided, the images are used as visual guidance. To
    animate a specific still as the opening frame, pass it as ``startFrameFileId`` instead."""

    video_file_ids: Optional[list[str]] = Field(default=UNSET, alias="videoFileIds")
    """Optional file ids of reference videos (e.g. ``["vg_file_..."]``). Upload files first via ``POST
    /v1/files/upload``, then pass the returned ids here. They are used as motion or style guidance for the generated
    video."""

    audio_file_ids: Optional[list[str]] = Field(default=UNSET, alias="audioFileIds")
    """Optional file ids of reference audio clips (e.g. ``["vg_file_..."]``) used for lip-sync from that recording.
    Upload files first via ``POST /v1/files/upload``, then pass the returned ids here. To have the model speak a line it
    generates itself, pass ``spokenDialogue`` instead (or in addition)."""

    spoken_dialogue: Optional[str] = Field(default=UNSET, alias="spokenDialogue")
    """Optional exact line the subject should speak as native, lip-synced speech in the generated clip. The model
    synthesizes the voice from this text. Can be the only input. Combine with a visual ``prompt``, ``startFrameFileId``,
    or reference media. Combine with ``audioFileIds`` when you also have a reference recording."""

    voice_description: Optional[str] = Field(default=UNSET, alias="voiceDescription")
    """Optional natural-language description of the voice that speaks ``spokenDialogue`` (for example, a warm, confident
    young man's voice). Used when ``spokenDialogue`` is set. When omitted, a clear natural voice is used."""

    generate_audio: bool = Field(default=False, alias="generateAudio")
    """When true, the generated video is guaranteed to include audio. When false, audio may still be present. Defaults
    to false."""

    suppress_background_music: bool = Field(default=False, alias="suppressBackgroundMusic")
    """When true, the generated clip will not include a musical soundtrack. Spoken dialogue and environmental sound are
    still allowed. Use this when you will add background music separately (for example at the project level). Defaults
    to false."""

    duration_seconds: OptionalNullable[int] = Field(default=UNSET, alias="durationSeconds")
    """Desired clip length in seconds. A whole number between 1 and 30. Defaults to 6 when omitted. The generated clip
    is clamped to the selected quality's supported range. This endpoint produces a single short clip. For longer,
    multi-scene, professionally edited videos, use a video workflow such as ``POST /v1/workflows/script-to-video``."""

    aspect_ratio: Optional[AspectRatio1] = Field(default=UNSET, alias="aspectRatio")
    """Aspect ratio for the generated video. Defaults to 16:9 when omitted."""

    quality: Optional[ModelQuality11OrStr] = UNSET
    """Video generation quality tier (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Optional; when omitted, your
    account's Default AI quality for video is used (change it at https://app.videogen.io/settings/account)."""

    content_policy_config: Optional[ContentPolicyConfig] = Field(default=UNSET, alias="contentPolicyConfig")
    """Controls how content-policy rejections are handled during generation."""

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


class GenerateVideoClipRequestDict(TypedDict):
    prompt: NotRequired[str]
    start_frame_file_id: NotRequired[str]
    image_file_ids: NotRequired[list[str]]
    video_file_ids: NotRequired[list[str]]
    audio_file_ids: NotRequired[list[str]]
    spoken_dialogue: NotRequired[str]
    voice_description: NotRequired[str]
    generate_audio: NotRequired[bool]
    suppress_background_music: NotRequired[bool]
    duration_seconds: NotRequired[int | None]
    aspect_ratio: NotRequired[AspectRatio1Dict]
    quality: NotRequired[ModelQuality11OrStr]
    content_policy_config: NotRequired[ContentPolicyConfigDict]
    watermark_mode: NotRequired[WatermarkModeOrStr]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
