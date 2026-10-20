from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .aspect_ratio2 import AspectRatio2, AspectRatio2Dict
from .content_policy_config import ContentPolicyConfig, ContentPolicyConfigDict
from .enums.model_quality10 import ModelQuality10OrStr
from .enums.watermark_mode import WatermarkMode, WatermarkModeOrStr


class GenerateImageRequest(SdkBaseModel):
    prompt: str
    """Text prompt describing the image to generate. When reference images are provided, the prompt describes the
    desired transformation."""

    image_file_ids: Optional[list[str]] = Field(default=UNSET, alias="imageFileIds")
    """Optional file ids of reference images (e.g. ``["vg_file_..."]``). Upload files first via ``POST
    /v1/files/upload``, then pass the returned ids here. Maximum 4 images. When provided, the model uses these as
    guidance for generation."""

    entity_ids: Optional[list[str]] = Field(default=UNSET, alias="entityIds")
    """Optional actor, product, or visual-style entity ids (e.g. ``["vg_enti_..."]``). The model uses each entity as
    identity/reference the same way in-app image generation does. Can be combined with ``imageFileIds``. A missing id
    returns not found; an inaccessible id returns a permission error."""

    aspect_ratio: Optional[AspectRatio2] = Field(default=UNSET, alias="aspectRatio")
    """Aspect ratio for the generated image. Defaults to 16:9 when omitted."""

    quality: Optional[ModelQuality10OrStr] = UNSET
    """Image generation quality tier. Optional; when omitted, your account's Default AI quality for images is used
    (change it at https://app.videogen.io/settings/account)."""

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


class GenerateImageRequestDict(TypedDict):
    prompt: str
    image_file_ids: NotRequired[list[str]]
    entity_ids: NotRequired[list[str]]
    aspect_ratio: NotRequired[AspectRatio2Dict]
    quality: NotRequired[ModelQuality10OrStr]
    content_policy_config: NotRequired[ContentPolicyConfigDict]
    watermark_mode: NotRequired[WatermarkModeOrStr]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
