from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .search_files_result import SearchFilesResult, SearchFilesResultDict


class SearchFilesResponse(SdkBaseModel):
    results: list[SearchFilesResult]


class SearchFilesResponseDict(TypedDict):
    results: list[SearchFilesResultDict]
