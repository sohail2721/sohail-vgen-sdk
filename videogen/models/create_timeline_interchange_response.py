from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateTimelineInterchangeResponse(SdkBaseModel):
    interchange_job_id: str = Field(alias="interchangeJobId")
    """Opaque timeline interchange job id (e.g. ``vg_inte_...``). Poll ``GET
    /v1/timeline-interchange/{interchangeJobId}`` for completion."""


class CreateTimelineInterchangeResponseDict(TypedDict):
    interchange_job_id: str
