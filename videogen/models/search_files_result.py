from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .file_info import FileInfo, FileInfoDict


class SearchFilesResult(SdkBaseModel):
    similarity: float
    """Cosine similarity between the query embedding and the file description embedding. Ranges from 0 (no match) to 1
    (identical). Values above 0.7 typically indicate strong relevance."""

    file: FileInfo
    """Metadata for a generated file. Obtain ids from tool results or ``GET /v1/files``."""


class SearchFilesResultDict(TypedDict):
    similarity: float
    file: FileInfoDict
