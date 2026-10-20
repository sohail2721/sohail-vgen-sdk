from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .entity import Entity, EntityDict


class ListEntitiesResponse(SdkBaseModel):
    entities: list[Entity]
    has_more: bool = Field(alias="hasMore")
    """When true, there are more entities available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the next
    page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class ListEntitiesResponseDict(TypedDict):
    entities: list[EntityDict]
    has_more: bool
    next_cursor: str | None
