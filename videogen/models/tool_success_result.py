from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.file_type1 import FileType1OrStr
from .file_info1 import FileInfo1, FileInfo1Dict


class ToolSuccessResult(SdkBaseModel):
    """Result for a single generated file. Only appears inside a succeeded execution's ``results``, so every field below
    is always present."""

    file_id: str = Field(alias="fileId")
    """File id for the generated asset."""

    type_: FileType1OrStr = Field(alias="type")
    """File type."""

    download_url: str | None = Field(alias="downloadUrl")
    """Private signed download URL for the generated file, valid for 7 days from when it was signed. Provided at the top
    level for convenience so you don't have to read it out of ``file``. When you GET a single execution it is
    automatically re-signed if within an hour of expiring; list endpoints do not re-sign, so there it may be expired
    (check ``downloadUrlExpiresAt``). See ``downloadUrlExpiresAt`` for the exact expiry. Null only in the rare case that
    the highest-quality rendition is still finalizing."""

    download_url_expires_at: int | None = Field(alias="downloadUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``downloadUrl`` expires. Null only when ``downloadUrl`` is null."""

    thumbnail_url: str | None = Field(alias="thumbnailUrl")
    """Private signed thumbnail URL for the generated file, valid for 7 days from when it was signed. Provided at the
    top level for convenience so you don't have to read it out of ``file``. Re-signed on the same terms as
    ``downloadUrl`` (single-execution GET re-signs when near expiry; list endpoints do not). Null for file types that
    have no thumbnail (e.g. audio)."""

    thumbnail_url_expires_at: int | None = Field(alias="thumbnailUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``thumbnailUrl`` expires. Null when there is no thumbnail URL."""

    file: FileInfo1
    """Hydrated file metadata with signed download URLs (always present and hydrated for a succeeded result). Its signed
    URLs follow the same 24-hour validity and automatic re-signing as ``downloadUrl``."""


class ToolSuccessResultDict(TypedDict):
    file_id: str
    type_: FileType1OrStr
    download_url: str | None
    download_url_expires_at: int | None
    thumbnail_url: str | None
    thumbnail_url_expires_at: int | None
    file: FileInfo1Dict
