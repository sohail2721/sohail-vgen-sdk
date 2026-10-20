from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .executed_tool import ExecutedTool, ExecutedToolDict


class ToolExecutionListResponse(SdkBaseModel):
    """Paginated list of API-started tool executions, most recently created first."""

    tool_executions: list[ExecutedTool] = Field(alias="toolExecutions")
    has_more: bool = Field(alias="hasMore")
    """When true, there are more executions available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the
    next page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class ToolExecutionListResponseDict(TypedDict):
    tool_executions: list[ExecutedToolDict]
    has_more: bool
    next_cursor: str | None
