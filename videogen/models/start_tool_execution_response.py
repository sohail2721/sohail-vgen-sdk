from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StartToolExecutionResponse(SdkBaseModel):
    """Returned when a tool execution is started. Use ``toolExecutionId`` to poll for results or cancel."""

    tool_execution_id: str = Field(alias="toolExecutionId")
    """Execution id (e.g. ``vg_tool_...``)."""


class StartToolExecutionResponseDict(TypedDict):
    tool_execution_id: str
