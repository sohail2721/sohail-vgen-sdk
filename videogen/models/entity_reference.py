from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EntityReference(SdkBaseModel):
    """A file attached to an entity as a reference image."""

    file_id: str = Field(alias="fileId")
    """The reference image file id (e.g. ``vg_file_...``). Hydrate it via ``GET /v1/files/{fileId}`` to fetch a viewable
    URL."""

    description: str
    """Optional description of the reference. Empty string when not set."""

    is_default: bool = Field(alias="isDefault")
    """When true, this is the entity's primary reference (used for its thumbnail)."""


class EntityReferenceDict(TypedDict):
    file_id: str
    description: str
    is_default: bool
