from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class GenerateSoundEffectRequest(SdkBaseModel):
    prompt: str
    """A text description of the sound effect to generate."""

    duration_seconds: OptionalNullable[float] = Field(default=UNSET, alias="durationSeconds")
    """Desired length of the sound effect in seconds, between 1 and 30. Defaults to about 10 seconds when omitted."""

    prompt_influence: OptionalNullable[float] = Field(default=UNSET, alias="promptInfluence")
    """How closely the generated sound effect follows the prompt, between 0 (more creative, more variation) and 1 (more
    literal, less variation). Defaults to a balanced value when omitted."""

    num_results: int = Field(default=1, alias="numResults")
    """Number of output results to generate. Defaults to 1."""

    is_output_temporary: bool = Field(default=False, alias="isOutputTemporary")
    """When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after
    which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding
    will be generated), so they will not appear in search results. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, generated files are hidden from the VideoGen Media page by default. They remain accessible through the
    API. Defaults to false."""


class GenerateSoundEffectRequestDict(TypedDict):
    prompt: str
    duration_seconds: NotRequired[float | None]
    prompt_influence: NotRequired[float | None]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
