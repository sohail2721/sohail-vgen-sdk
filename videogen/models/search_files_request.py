from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class SearchFilesRequest(SdkBaseModel):
    query: str
    """Natural-language search query. The text is embedded and compared against file description vectors using cosine
    similarity."""

    num_results: int = Field(default=10, alias="numResults")
    """Number of results to return (1-100). Defaults to 10."""

    self_only: bool = Field(default=False, alias="selfOnly")
    """When true, only files created by the calling API key's user are returned. When false (default), all files
    accessible to the team are included."""


class SearchFilesRequestDict(TypedDict):
    query: str
    num_results: NotRequired[int]
    self_only: NotRequired[bool]
