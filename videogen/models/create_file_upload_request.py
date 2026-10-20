from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.file_type2 import FileType2OrStr
from .transcript import Transcript, TranscriptDict


class CreateFileUploadRequest(SdkBaseModel):
    type_: Optional[FileType2OrStr] = Field(default=UNSET, alias="type")
    """The type of file to upload. Optional; when omitted, the type is inferred after upload processing completes."""

    display_name: str = Field(alias="displayName")
    """Display name for the uploaded file."""

    is_temporary: bool = Field(default=False, alias="isTemporary")
    """When true, the file is temporary. Temporary files are guaranteed to be available for 24 hours, after which they
    may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding will be
    generated), so they will not appear in search results. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, the file is hidden from the VideoGen Media page by default. It remains accessible through the API.
    Defaults to false."""

    transcript: OptionalNullable[Transcript] = UNSET
    """Optional pre-computed transcript for an audio or video upload, as timed ``words``. When provided, transcription
    is skipped and caption timing matches your transcript. Ignored for non-audio/video files."""


class CreateFileUploadRequestDict(TypedDict):
    type_: NotRequired[FileType2OrStr]
    display_name: str
    is_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
    transcript: NotRequired[TranscriptDict | None]
