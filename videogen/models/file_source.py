from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.file_source_status import FileSourceStatusOrStr


class FileSource(SdkBaseModel):
    """A rendition source for a file (e.g. thumbnail, preview, download). Contains a signed URL and metadata."""

    status: FileSourceStatusOrStr
    """``pending``: asset is still processing or has not been hydrated yet. ``ready``: signed URL is available.
    ``failed``: rendition generation failed. ``skipped``: rendition does not apply to this file type (e.g. thumbnail for
    audio)."""

    url: OptionalNullable[str] = UNSET
    """Signed URL. Present when status is ``ready`` and file has been recently hydrated. If missing, call the hydrate
    endpoint."""

    expires_at: OptionalNullable[int] = Field(default=UNSET, alias="expiresAt")
    """Seconds since epoch (Unix timestamp) when the signed URL expires."""

    width: OptionalNullable[int] = UNSET
    """Rendition width in pixels, when known."""

    height: OptionalNullable[int] = UNSET
    """Rendition height in pixels, when known."""

    file_bytes: OptionalNullable[int] = Field(default=UNSET, alias="fileBytes")
    """File size in bytes, when known."""


class FileSourceDict(TypedDict):
    status: FileSourceStatusOrStr
    url: NotRequired[str | None]
    expires_at: NotRequired[int | None]
    width: NotRequired[int | None]
    height: NotRequired[int | None]
    file_bytes: NotRequired[int | None]
