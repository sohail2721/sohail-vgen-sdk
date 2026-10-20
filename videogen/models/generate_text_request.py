from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.model_quality13 import ModelQuality13OrStr


class GenerateTextRequest(SdkBaseModel):
    prompt: str
    """The instruction or content to generate text from."""

    system: OptionalNullable[str] = UNSET
    """Optional system instructions that steer the model's role, tone, and constraints."""

    quality: Optional[ModelQuality13OrStr] = UNSET
    """Text generation quality tier. Optional; when omitted, your account's Default AI quality for text is used (change
    it at https://app.videogen.io/settings/account)."""

    temperature: Optional[float] = UNSET
    """Sampling temperature. Higher values produce more varied output. Defaults to the model's default."""

    max_output_tokens: int = Field(default=512, alias="maxOutputTokens")
    """Maximum number of tokens to generate. Defaults to 512."""


class GenerateTextRequestDict(TypedDict):
    prompt: str
    system: NotRequired[str | None]
    quality: NotRequired[ModelQuality13OrStr]
    temperature: NotRequired[float]
    max_output_tokens: NotRequired[int]
