from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class ContentPolicyConfig(SdkBaseModel):
    """Controls how content-policy rejections are handled during generation."""

    max_prompt_rewrites: int = Field(default=0, alias="maxPromptRewrites")
    """Maximum number of automatic prompt rewrites to attempt after a content-policy rejection before failing. Must be
    an integer between 0 and 4. 0 (the default) fails on the first rejection and returns the moderation error so you can
    revise the prompt yourself. Higher values let the request automatically rephrase and retry the prompt."""


class ContentPolicyConfigDict(TypedDict):
    max_prompt_rewrites: NotRequired[int]
