from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.model_quality3 import ModelQuality3OrStr


class RemixAction11(SdkBaseModel):
    """Re-narrate every AI-voiceover asset in the project with a new voice and optional actor avatar, replacing each
    narration in place. Runs asynchronously: text-to-speech is re-fired per asset with the original narration text. If
    the project has no AI-narrated assets, the action is skipped and completes successfully without changing
    anything."""

    type_: Literal["CHANGE_NARRATOR"] = Field(default="CHANGE_NARRATOR", alias="type")
    """Discriminator value: CHANGE_NARRATOR"""

    voice_id: str = Field(alias="voiceId")
    """Catalog ``displayName`` (e.g. ``Matilda``) or voice id from ``GET /v1/resources/tts-voices`` (e.g.
    ``vg_voic_...``) to re-narrate with."""

    actor_entity_id: OptionalNullable[str] = Field(default=UNSET, alias="actorEntityId")
    """Recommended. Optional id of a built-in stock actor or an ACTOR entity (e.g. ``vg_enti_...``) with an image
    reference. When set, narration is delivered by that actor avatar. Omit or pass ``null`` for voiceover without an
    avatar."""

    avatar_quality: Optional[ModelQuality3OrStr] = Field(default=UNSET, alias="avatarQuality")
    """Avatar generation quality tier. Applies when ``actorEntityId`` is provided. Optional; when omitted, your
    account's Default AI quality for avatars is used."""

    voice_speed: OptionalNullable[float] = Field(default=UNSET, alias="voiceSpeed")
    """Speech rate multiplier, between 0.5 (half speed) and 2 (double speed). Omit or pass ``null`` to keep each asset's
    current speed."""


class RemixAction11Dict(TypedDict):
    type_: Literal["CHANGE_NARRATOR"]
    voice_id: str
    actor_entity_id: NotRequired[str | None]
    avatar_quality: NotRequired[ModelQuality3OrStr]
    voice_speed: NotRequired[float | None]
