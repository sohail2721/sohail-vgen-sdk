from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.entity_entity_type import EntityEntityTypeOrStr


class CreateEntityRequest(SdkBaseModel):
    entity_type: EntityEntityTypeOrStr = Field(alias="entityType")
    """ACTOR features a consistent character; PRODUCT features a consistent product or object; VISUAL_STYLE guides the
    look of generated images; SLIDESHOW_THEME is a shared slide design system (fonts, colors, layout) applied to every
    slide of a slideshow-to-video deck."""

    name: str
    """Display name."""

    description: Optional[str] = UNSET
    """Optional description."""


class CreateEntityRequestDict(TypedDict):
    entity_type: EntityEntityTypeOrStr
    name: str
    description: NotRequired[str]
