from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemixAction13(SdkBaseModel):
    """Generate a background music track from a text prompt and set it as the project's background music, replacing any
    existing track. Runs asynchronously."""

    type_: Literal["GENERATE_MUSIC"] = Field(default="GENERATE_MUSIC", alias="type")
    """Discriminator value: GENERATE_MUSIC"""

    prompt: str
    """Describe the music to generate (e.g. "upbeat corporate background music with a driving beat")."""


class RemixAction13Dict(TypedDict):
    type_: Literal["GENERATE_MUSIC"]
    prompt: str
