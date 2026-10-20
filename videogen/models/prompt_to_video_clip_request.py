from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .aspect_ratio1 import AspectRatio1, AspectRatio1Dict
from .enums.model_quality9 import ModelQuality9OrStr


class PromptToVideoClipRequest(SdkBaseModel):
    """Creates a project from a text prompt and generates one short AI video clip. VideoGen generates an opening frame
    from the prompt (optionally guided by reference images), then animates that frame into a video inside an editable
    project. This workflow does not accept ``remixActions``. For a standalone clip without a project, use ``POST
    /v1/tools/generate-video-clip``. For longer narrated multi-scene videos, use ``POST
    /v1/workflows/script-to-video``."""

    prompt: str
    """Text prompt describing the video to generate (e.g. ``A golden retriever running through a sunlit meadow in slow
    motion, cinematic``)."""

    image_file_ids: Optional[list[str]] = Field(default=UNSET, alias="imageFileIds")
    """Optional ids of previously uploaded reference images (e.g. ``vg_file_...``) that guide the opening frame. Upload
    files via ``POST /v1/files/upload`` first."""

    duration_seconds: Optional[int] = Field(default=UNSET, alias="durationSeconds")
    """Desired clip length in whole seconds (1 to 30). Defaults to 10. The generated clip is clamped to the selected
    quality's supported range."""

    aspect_ratio: Optional[AspectRatio1] = Field(default=UNSET, alias="aspectRatio")
    """Aspect ratio for the generated video. Defaults to 16:9 when omitted."""

    quality: Optional[ModelQuality9OrStr] = UNSET
    """Video generation quality tier (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Also used for the opening-frame
    image. Optional; when omitted, your account's Default AI quality for video is used (change it at
    https://app.videogen.io/settings/account)."""

    is_output_temporary: bool = Field(default=False, alias="isOutputTemporary")
    """When true, the generated OUTPUT files (the opening-frame image and the video clip) are created as temporary:
    guaranteed available for 24 hours, after which they may be archived and later deleted. Use this when your
    integration downloads or re-hosts the results itself and does not need VideoGen to retain them. The project and its
    metadata are unaffected. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, generated files are hidden from the VideoGen Media page by default. They remain accessible through the
    API. Defaults to false."""


class PromptToVideoClipRequestDict(TypedDict):
    prompt: str
    image_file_ids: NotRequired[list[str]]
    duration_seconds: NotRequired[int]
    aspect_ratio: NotRequired[AspectRatio1Dict]
    quality: NotRequired[ModelQuality9OrStr]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
