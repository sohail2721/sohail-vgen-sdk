from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .project_response import ProjectResponse, ProjectResponseDict


class ListProjectsResponse(SdkBaseModel):
    """Paginated list of projects, most recently updated first. By default only API-created projects are included; pass
    ``includeUiProjects=true`` on the request to also include dashboard-created projects."""

    projects: list[ProjectResponse]
    has_more: bool = Field(alias="hasMore")
    """When true, there are more projects available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the next
    page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class ListProjectsResponseDict(TypedDict):
    projects: list[ProjectResponseDict]
    has_more: bool
    next_cursor: str | None
