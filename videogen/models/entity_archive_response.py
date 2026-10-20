from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class EntityArchiveResponse(SdkBaseModel):
    entity_id: str = Field(alias="entityId")
    """The id of the archived entity."""

    archived: bool
    """Always true on success."""


class EntityArchiveResponseDict(TypedDict):
    entity_id: str
    archived: bool
