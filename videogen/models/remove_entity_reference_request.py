from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemoveEntityReferenceRequest(SdkBaseModel):
    file_id: str = Field(alias="fileId")
    """The file id (e.g. ``vg_file_...``) of the reference to remove."""


class RemoveEntityReferenceRequestDict(TypedDict):
    file_id: str
