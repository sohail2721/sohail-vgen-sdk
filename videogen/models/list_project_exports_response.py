from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .project_export import ProjectExport, ProjectExportDict


class ListProjectExportsResponse(SdkBaseModel):
    exports: list[ProjectExport]
    """Fully hydrated exports for this project, newest first. Each includes status, signed download/thumbnail URLs, and
    the embedded ``file``."""

    has_more: bool = Field(alias="hasMore")
    """When true, there are more exports available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the next
    page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class ListProjectExportsResponseDict(TypedDict):
    exports: list[ProjectExportDict]
    has_more: bool
    next_cursor: str | None
