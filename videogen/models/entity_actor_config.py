from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class EntityActorConfig(SdkBaseModel):
    """Read-only voice and avatar summary for an ACTOR entity. Always null for non-ACTOR entities."""

    voice_display_name: OptionalNullable[str] = Field(default=UNSET, alias="voiceDisplayName")
    """Display name of the actor's voice when one is configured. Null otherwise."""

    has_voice: bool = Field(alias="hasVoice")
    """True when the actor has a configured voice."""

    has_avatar_presenter: bool = Field(alias="hasAvatarPresenter")
    """True when the actor has a built-in presenter or image reference that can be used with ``actorEntityId`` for
    avatar generation."""


class EntityActorConfigDict(TypedDict):
    voice_display_name: NotRequired[str | None]
    has_voice: bool
    has_avatar_presenter: bool
