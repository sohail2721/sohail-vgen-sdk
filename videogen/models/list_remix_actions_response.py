from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .remix_action_run import RemixActionRun, RemixActionRunDict


class ListRemixActionsResponse(SdkBaseModel):
    remix_actions: list[RemixActionRun] = Field(alias="remixActions")
    """Remix actions for the project, most recent first."""

    has_more: bool = Field(alias="hasMore")
    """When true, there are more remix actions available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the
    next page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class ListRemixActionsResponseDict(TypedDict):
    remix_actions: list[RemixActionRunDict]
    has_more: bool
    next_cursor: str | None
