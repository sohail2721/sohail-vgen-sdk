from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.file_info_scope import FileInfoScopeOrStr
from .enums.file_type import FileTypeOrStr
from .file_analysis_metadata1 import FileAnalysisMetadata1, FileAnalysisMetadata1Dict
from .file_source import FileSource, FileSourceDict
from .transcript import Transcript, TranscriptDict


class FileInfo(SdkBaseModel):
    """Metadata for a generated file. Obtain ids from tool results or ``GET /v1/files``."""

    file_id: str = Field(alias="fileId")
    """File id (e.g. ``vg_file_...``)."""

    type_: OptionalNullable[FileTypeOrStr] = Field(default=UNSET, alias="type")
    """File type. Null when the file is still being processed and the type has not yet been determined."""

    scope: FileInfoScopeOrStr
    """File scope.

    - ``GLOBAL``: user-uploaded or standalone generated files that persist indefinitely.
    - ``PROJECT``: project-specific files (e.g. text-to-speech clips in a generated project).
    - ``EXPORT``: project exports.
    - ``TEMPORARY``: short-lived files guaranteed to be available for 24 hours, after which they may be archived at any
        time. Not analyzed (no description, transcript, or embedding).
    - ``ENTITY``: files attached to a reusable entity (e.g. a voice sample for an actor), shared across your team."""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Display name for the file."""

    description: OptionalNullable[str] = UNSET
    duration_seconds: OptionalNullable[float] = Field(default=UNSET, alias="durationSeconds")
    """Duration in seconds for video and audio files. Null for images."""

    transcript: OptionalNullable[Transcript] = UNSET
    """Timed transcript for video and audio files, when available, as a ``Transcript`` object with timed ``words``. Null
    for images or when no transcript has been generated. For plain transcript text, use ``transcriptText``."""

    transcript_text: OptionalNullable[str] = Field(default=UNSET, alias="transcriptText")
    """Plain transcript text for video and audio files, when available. Null for images or when no transcript has been
    generated."""

    download_url: OptionalNullable[str] = Field(default=UNSET, alias="downloadUrl")
    """Private signed URL for the highest-quality downloadable rendition, provided at the top level for convenience.
    Valid for 7 days from when it was signed. ``null`` when the rendition is still processing or the URL has not been
    signed yet. See ``downloadUrlExpiresAt`` for the exact expiry and ``downloadSource`` for the full rendition
    metadata; call ``POST /v1/files/{fileId}/hydrate`` to refresh it."""

    download_url_expires_at: OptionalNullable[int] = Field(default=UNSET, alias="downloadUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``downloadUrl`` expires. ``null`` when ``downloadUrl`` is null."""

    thumbnail_url: OptionalNullable[str] = Field(default=UNSET, alias="thumbnailUrl")
    """Private signed URL for the thumbnail rendition, provided at the top level for convenience. Valid for 7 days from
    when it was signed. ``null`` for file types that have no thumbnail (e.g. audio) or when it has not been signed yet.
    See ``thumbnailSource`` for the full rendition metadata."""

    thumbnail_url_expires_at: OptionalNullable[int] = Field(default=UNSET, alias="thumbnailUrlExpiresAt")
    """Seconds since epoch (Unix timestamp) when ``thumbnailUrl`` expires. ``null`` when ``thumbnailUrl`` is null."""

    thumbnail_source: OptionalNullable[FileSource] = Field(default=UNSET, alias="thumbnailSource")
    """Thumbnail image source. Populated after hydration."""

    preview_source: OptionalNullable[FileSource] = Field(default=UNSET, alias="previewSource")
    """Preview rendition source (720p for video, resized for images). Populated after hydration."""

    download_source: OptionalNullable[FileSource] = Field(default=UNSET, alias="downloadSource")
    """Highest-quality downloadable rendition. Populated after hydration."""

    hls_source: OptionalNullable[FileSource] = Field(default=UNSET, alias="hlsSource")
    """Private HLS streaming source. Populated for video and audio files once streaming renditions are ready. Uses a
    signed token; treat like other signed sources."""

    is_public_preview_enabled: Optional[bool] = Field(default=UNSET, alias="isPublicPreviewEnabled")
    """Whether public preview is enabled for this file. When true, ``staticPublicPreviewSource`` is populated for all
    file types. For video and audio, ``publicHlsUrl`` and ``publicPlaybackId`` are also populated once embed streaming
    is ready."""

    static_public_preview_source: OptionalNullable[FileSource] = Field(default=UNSET, alias="staticPublicPreviewSource")
    """Permanent public URL for the file's highest-quality rendition. Populated when ``isPublicPreviewEnabled`` is true.
    Does not expire (``expiresAt`` is null). Use for direct links to images, downloads, or any file type. For embedded
    video or audio players, prefer ``publicPlaybackId``."""

    public_hls_url: OptionalNullable[str] = Field(default=UNSET, alias="publicHlsUrl")
    """Public HLS streaming URL for video and audio. Only present when ``isPublicPreviewEnabled`` is true and embed
    streaming is ready. Prefer ``publicPlaybackId`` with ``@videogen/player`` for embeds."""

    public_playback_id: OptionalNullable[str] = Field(default=UNSET, alias="publicPlaybackId")
    """Encoded public playback id (e.g. ``vg_play_...``) for video and audio embeds. Pass this to ``@videogen/player``
    or ``@videogen/player-react``. Only present when ``isPublicPreviewEnabled`` is true and embed streaming is ready.
    For a permanent direct file URL (any type), use ``staticPublicPreviewSource`` instead."""

    source_tool_type: Optional[str] = Field(default=UNSET, alias="sourceToolType")
    """Tool type that generated this file (e.g. ``GENERATE_IMAGE``, ``TEXT_TO_SPEECH``). Only present when the file was
    created by a tool execution."""

    source_tool_execution_id: Optional[str] = Field(default=UNSET, alias="sourceToolExecutionId")
    """Execution id of the tool call that generated this file (e.g. ``vg_tool_...``). Only present when the file was
    created by a tool execution."""

    file_analysis_metadata: Optional[FileAnalysisMetadata1] = Field(default=UNSET, alias="fileAnalysisMetadata")
    """Background analysis state for the file (used to populate ``description``, ``transcript``, ``durationSeconds``,
    and the search embedding). Omitted when the file was returned via a path that does not check analysis progress (e.g.
    tool-result inline files and webhook payloads)."""


class FileInfoDict(TypedDict):
    file_id: str
    type_: NotRequired[FileTypeOrStr | None]
    scope: FileInfoScopeOrStr
    display_name: NotRequired[str]
    description: NotRequired[str | None]
    duration_seconds: NotRequired[float | None]
    transcript: NotRequired[TranscriptDict | None]
    transcript_text: NotRequired[str | None]
    download_url: NotRequired[str | None]
    download_url_expires_at: NotRequired[int | None]
    thumbnail_url: NotRequired[str | None]
    thumbnail_url_expires_at: NotRequired[int | None]
    thumbnail_source: NotRequired[FileSourceDict | None]
    preview_source: NotRequired[FileSourceDict | None]
    download_source: NotRequired[FileSourceDict | None]
    hls_source: NotRequired[FileSourceDict | None]
    is_public_preview_enabled: NotRequired[bool]
    static_public_preview_source: NotRequired[FileSourceDict | None]
    public_hls_url: NotRequired[str | None]
    public_playback_id: NotRequired[str | None]
    source_tool_type: NotRequired[str]
    source_tool_execution_id: NotRequired[str]
    file_analysis_metadata: NotRequired[FileAnalysisMetadata1Dict]
