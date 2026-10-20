from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.model_quality2 import ModelQuality2OrStr


class RemixAction9(SdkBaseModel):
    """Restyle every eligible still image in the project to a new look (image-to-image), replacing each image in place.
    Eligible images are non-SVG image assets backed by an uploaded or generated file. Runs asynchronously: one restyled
    image is generated per eligible image. If the project has no eligible images, the action is skipped and completes
    successfully without changing anything."""

    type_: Literal["REGENERATE_IMAGES"] = Field(default="REGENERATE_IMAGES", alias="type")
    """Discriminator value: REGENERATE_IMAGES"""

    style_prompt: str = Field(alias="stylePrompt")
    """Describe the visual style to apply to every image (e.g. "watercolor painting", "cinematic film still")."""

    quality: Optional[ModelQuality2OrStr] = UNSET
    """Image generation quality tier for the restyled images. Optional; when omitted, your account's Default AI quality
    for images is used (change it at https://app.videogen.io/settings/account)."""


class RemixAction9Dict(TypedDict):
    type_: Literal["REGENERATE_IMAGES"]
    style_prompt: str
    quality: NotRequired[ModelQuality2OrStr]
