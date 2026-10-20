from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .file_info import FileInfo, FileInfoDict


class GetFilesResponse(SdkBaseModel):
    files: list[FileInfo]
    has_more: bool = Field(alias="hasMore")
    """When true, there are more files available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the next
    page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class GetFilesResponseDict(TypedDict):
    files: list[FileInfoDict]
    has_more: bool
    next_cursor: str | None
