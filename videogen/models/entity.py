from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .entity_actor_config import EntityActorConfig, EntityActorConfigDict
from .entity_reference import EntityReference, EntityReferenceDict
from .enums.entity_entity_type import EntityEntityTypeOrStr


class Entity(SdkBaseModel):
    """A reusable actor, product, visual style, or slideshow theme. Attach its reference images to workflows for
    consistent characters, looks, and slide designs."""

    entity_id: str = Field(alias="entityId")
    """The entity id (e.g. ``vg_enti_...``)."""

    entity_type: EntityEntityTypeOrStr = Field(alias="entityType")
    """ACTOR features a consistent character; PRODUCT features a consistent product or object; VISUAL_STYLE guides the
    look of generated images; SLIDESHOW_THEME is a shared slide design system (fonts, colors, layout) applied to every
    slide of a slideshow-to-video deck."""

    name: str
    """Display name."""

    description: str
    """Optional description. Empty string when not set."""

    actor_config: OptionalNullable[EntityActorConfig] = Field(default=UNSET, alias="actorConfig")
    """Voice and presenter summary for ACTOR entities. Null for non-ACTOR entities."""

    references: list[EntityReference]
    """Reference images attached to the entity."""

    created_at: int = Field(alias="createdAt")
    """Seconds since epoch (Unix timestamp) when the entity was created."""

    updated_at: int = Field(alias="updatedAt")
    """Seconds since epoch (Unix timestamp) when the entity was last updated."""

    is_built_in: Optional[bool] = Field(default=UNSET, alias="isBuiltIn")
    """When true, this is a VideoGen catalog entity. Built-in entities cannot be updated, archived, or have references
    added or removed."""


class EntityDict(TypedDict):
    entity_id: str
    entity_type: EntityEntityTypeOrStr
    name: str
    description: str
    actor_config: NotRequired[EntityActorConfigDict | None]
    references: list[EntityReferenceDict]
    created_at: int
    updated_at: int
    is_built_in: NotRequired[bool]
