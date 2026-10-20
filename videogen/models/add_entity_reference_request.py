from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddEntityReferenceRequest(SdkBaseModel):
    file_id: str = Field(alias="fileId")
    """The file id (e.g. ``vg_file_...``) of an image to attach as a reference."""

    description: Optional[str] = UNSET
    """Optional description of the reference."""

    is_default: bool = Field(default=False, alias="isDefault")
    """When true, make this the entity's primary reference (used for its thumbnail)."""


class AddEntityReferenceRequestDict(TypedDict):
    file_id: str
    description: NotRequired[str]
    is_default: NotRequired[bool]
