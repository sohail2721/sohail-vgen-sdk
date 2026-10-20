from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RemixAction7(SdkBaseModel):
    """Tighten every transcript in the project by removing silent pauses and/or filler words. Useful for polishing
    narration captured from raw recordings."""

    type_: Literal["CLEAN_UP_TRANSCRIPT"] = Field(default="CLEAN_UP_TRANSCRIPT", alias="type")
    """Discriminator value: CLEAN_UP_TRANSCRIPT"""

    remove_fillers: OptionalNullable[bool] = Field(default=UNSET, alias="removeFillers")
    """Remove filler words ("um", "uh", …). Defaults to ``true``."""

    remove_pauses: OptionalNullable[bool] = Field(default=UNSET, alias="removePauses")
    """Remove silent pauses longer than ``minPauseSeconds``. Defaults to ``true``."""

    filler_words: OptionalNullable[list[str]] = Field(default=UNSET, alias="fillerWords")
    """Override the filler-word list to remove. Omit or pass ``null`` to use the built-in defaults."""

    min_pause_seconds: OptionalNullable[float] = Field(default=UNSET, alias="minPauseSeconds")
    """Shortest pause (in seconds) to remove; pauses below this stay. Omit or pass ``null`` to use the default
    threshold."""


class RemixAction7Dict(TypedDict):
    type_: Literal["CLEAN_UP_TRANSCRIPT"]
    remove_fillers: NotRequired[bool | None]
    remove_pauses: NotRequired[bool | None]
    filler_words: NotRequired[list[str] | None]
    min_pause_seconds: NotRequired[float | None]
