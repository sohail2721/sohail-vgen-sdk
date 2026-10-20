from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .api_error_model import ApiErrorModel, ApiErrorModelDict
from .enums.job_status import JobStatusOrStr
from .file_info import FileInfo, FileInfoDict


class ProjectExport(SdkBaseModel):
    export_id: str = Field(alias="exportId")
    """Opaque export id (e.g. ``vg_expo_...``) matching the original request."""

    project_id: str = Field(alias="projectId")
    """Id of the exported project (e.g. ``vg_proj_...``)."""

    status: JobStatusOrStr
    """Lifecycle status shared by every asynchronous job (tool executions, workflow runs, remix actions, project
    exports, and timeline interchange jobs). ``pending`` and ``running`` are in-progress; ``succeeded``, ``failed``, and
    ``cancelled`` are terminal."""

    progress_percentage: float = Field(alias="progressPercentage")
    """Completion progress for the current attempt (0-100). Always ``100`` when ``status`` is ``succeeded``."""

    attempt_index: int = Field(alias="attemptIndex")
    """Zero-based index of the current or most recent export attempt."""

    download_url: str | None = Field(alias="downloadUrl")
    """Private signed MP4 download URL, valid for 7 days from when it was signed. Always present as a field; ``null``
    until ``status`` is ``succeeded``. This endpoint automatically re-signs the URL when it is within an hour of
    expiring, so a fresh call to get the export always returns a URL valid long enough to use. See
    ``downloadUrlExpiresAt`` for the exact expiry. To fetch a fresh URL directly from the underlying file at any time,
    use ``exportFileId`` with the hydrate-file endpoint."""

    download_url_expires_at: int | None = Field(alias="downloadUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``downloadUrl`` expires. ``null`` while ``downloadUrl`` is null."""

    thumbnail_url: str | None = Field(alias="thumbnailUrl")
    """Private signed thumbnail URL, valid for 7 days from when it was signed. Always present as a field; ``null`` until
    ``status`` is ``succeeded`` (and when no thumbnail is available). Re-signed automatically on the same terms as
    ``downloadUrl``."""

    thumbnail_url_expires_at: int | None = Field(alias="thumbnailUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``thumbnailUrl`` expires. ``null`` while ``thumbnailUrl`` is null."""

    export_file_id: str | None = Field(alias="exportFileId")
    """File id (e.g. ``vg_file_...``) of the exported MP4. Always present as a field; ``null`` until ``status`` is
    ``succeeded``. Pass it to ``POST /v1/files/{fileId}/hydrate`` to fetch fresh signed URLs directly from the file at
    any time, which is useful once the 24-hour URLs above have expired."""

    file: FileInfo | None
    """Hydrated export file metadata with signed download URLs. Always present as a field; ``null`` until ``status`` is
    ``succeeded``. Its signed URLs follow the same 24-hour validity and automatic re-signing as ``downloadUrl``."""

    error: ApiErrorModel | None
    """Error details. Always present as a field; ``null`` unless ``status`` is ``failed``."""


class ProjectExportDict(TypedDict):
    export_id: str
    project_id: str
    status: JobStatusOrStr
    progress_percentage: float
    attempt_index: int
    download_url: str | None
    download_url_expires_at: int | None
    thumbnail_url: str | None
    thumbnail_url_expires_at: int | None
    export_file_id: str | None
    file: FileInfoDict | None
    error: ApiErrorModelDict | None
