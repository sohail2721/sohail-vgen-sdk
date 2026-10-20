from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ExportProjectResponse(SdkBaseModel):
    export_id: str = Field(alias="exportId")
    """Opaque export id (e.g. ``vg_expo_...``). Poll ``GET /v1/projects/{projectId}/exports/{exportId}`` or subscribe to
    webhooks for completion."""


class ExportProjectResponseDict(TypedDict):
    export_id: str
