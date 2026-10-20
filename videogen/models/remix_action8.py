from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.model_quality1 import ModelQuality1OrStr


class RemixAction8(SdkBaseModel):
    """Animate every eligible still image in the project into a short AI video clip (image-to-video), replacing each
    image in place. Eligible images are non-SVG image assets backed by an uploaded or stock file. Runs asynchronously:
    one clip is generated per image. If the project has no eligible images, the action is skipped and completes
    successfully without changing anything (for example, a project whose timeline is already all video clips)."""

    type_: Literal["CONVERT_IMAGES_TO_VIDEOS"] = Field(default="CONVERT_IMAGES_TO_VIDEOS", alias="type")
    """Discriminator value: CONVERT_IMAGES_TO_VIDEOS"""

    motion_prompt: OptionalNullable[str] = Field(default=UNSET, alias="motionPrompt")
    """Describe the motion to apply to every image (e.g. "slow cinematic push-in"). Omit or pass ``null`` for automatic
    motion."""

    mute_output_videos: OptionalNullable[bool] = Field(default=UNSET, alias="muteOutputVideos")
    """Mute the generated clips and suppress generated background music. Recommended when the clips sit behind a
    voiceover. Defaults to ``true``."""

    quality: Optional[ModelQuality1OrStr] = UNSET
    """Video generation quality tier for the image-to-video conversions (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``).
    Optional; when omitted, your account's Default AI quality for video is used (change it at
    https://app.videogen.io/settings/account)."""


class RemixAction8Dict(TypedDict):
    type_: Literal["CONVERT_IMAGES_TO_VIDEOS"]
    motion_prompt: NotRequired[str | None]
    mute_output_videos: NotRequired[bool | None]
    quality: NotRequired[ModelQuality1OrStr]
