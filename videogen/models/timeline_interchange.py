from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .api_error_model import ApiErrorModel, ApiErrorModelDict
from .enums.job_status import JobStatusOrStr
from .enums.timeline_interchange_format import TimelineInterchangeFormatOrStr
from .enums.timeline_interchange_media_delivery import TimelineInterchangeMediaDeliveryOrStr
from .file_info import FileInfo, FileInfoDict


class TimelineInterchange(SdkBaseModel):
    interchange_job_id: str = Field(alias="interchangeJobId")
    """Opaque timeline interchange job id (e.g. ``vg_inte_...``) matching the original request."""

    project_id: str = Field(alias="projectId")
    """Id of the source project (e.g. ``vg_proj_...``)."""

    format: TimelineInterchangeFormatOrStr
    """Editor interchange document format. ``FCPXML`` is Final Cut Pro (also imported by DaVinci Resolve and others).
    ``PREMIERE_XML`` is the Final Cut 7 ``xmeml`` XML that Adobe Premiere Pro imports natively. ``OTIO`` is
    OpenTimelineIO, the vendor-neutral format. ``SRT`` is a SubRip caption sidecar."""

    media_delivery: TimelineInterchangeMediaDeliveryOrStr = Field(alias="mediaDelivery")
    """How the interchange document references media. ``REMOTE_URLS`` produces a single document that links to signed
    media URLs. ``BUNDLE`` produces a zip containing the document plus every referenced media file, referenced by
    relative path, for durable offline relinking."""

    status: JobStatusOrStr
    """Lifecycle status shared by every asynchronous job (tool executions, workflow runs, remix actions, project
    exports, and timeline interchange jobs). ``pending`` and ``running`` are in-progress; ``succeeded``, ``failed``, and
    ``cancelled`` are terminal."""

    progress_percentage: float = Field(alias="progressPercentage")
    """Completion progress for the current attempt (0-100). Always ``100`` when ``status`` is ``succeeded``."""

    attempt_index: int = Field(alias="attemptIndex")
    """Zero-based index of the current or most recent job attempt."""

    download_url: str | None = Field(alias="downloadUrl")
    """Private signed download URL for the interchange document (or the media bundle zip when ``mediaDelivery`` is
    ``BUNDLE``), valid for 7 days from when it was signed. Always present as a field; ``null`` until ``status`` is
    ``succeeded``. This endpoint automatically re-signs the URL when it is within an hour of expiring. To fetch a fresh
    URL directly from the underlying file at any time, use ``interchangeFileId`` with the hydrate-file endpoint."""

    download_url_expires_at: int | None = Field(alias="downloadUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``downloadUrl`` expires. ``null`` while ``downloadUrl`` is null."""

    interchange_file_id: str | None = Field(alias="interchangeFileId")
    """File id (e.g. ``vg_file_...``) of the interchange document or bundle zip. Always present as a field; ``null``
    until ``status`` is ``succeeded``. Pass it to ``POST /v1/files/{fileId}/hydrate`` to fetch fresh signed URLs
    directly from the file at any time."""

    file: FileInfo | None
    """Hydrated interchange file metadata with a signed download URL. Always present as a field; ``null`` until
    ``status`` is ``succeeded``. Its signed URL follows the same 24-hour validity and automatic re-signing as
    ``downloadUrl``."""

    error: ApiErrorModel | None
    """Error details. Always present as a field; ``null`` unless ``status`` is ``failed``."""


class TimelineInterchangeDict(TypedDict):
    interchange_job_id: str
    project_id: str
    format: TimelineInterchangeFormatOrStr
    media_delivery: TimelineInterchangeMediaDeliveryOrStr
    status: JobStatusOrStr
    progress_percentage: float
    attempt_index: int
    download_url: str | None
    download_url_expires_at: int | None
    interchange_file_id: str | None
    file: FileInfoDict | None
    error: ApiErrorModelDict | None
