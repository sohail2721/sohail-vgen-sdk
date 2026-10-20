from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FileUploadResponse(SdkBaseModel):
    file_id: str = Field(alias="fileId")
    """The file id to use in subsequent API calls (e.g. ``vg_file_...``)."""

    upload_url: str = Field(alias="uploadUrl")
    """Pre-signed URL. PUT the raw file bytes to this URL to complete the upload."""


class FileUploadResponseDict(TypedDict):
    file_id: str
    upload_url: str
