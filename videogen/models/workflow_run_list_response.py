from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .workflow_run import WorkflowRun, WorkflowRunDict


class WorkflowRunListResponse(SdkBaseModel):
    """Paginated list of API-started workflow runs, most recently created first."""

    workflow_runs: list[WorkflowRun] = Field(alias="workflowRuns")
    has_more: bool = Field(alias="hasMore")
    """When true, there are more runs available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the next
    page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class WorkflowRunListResponseDict(TypedDict):
    workflow_runs: list[WorkflowRunDict]
    has_more: bool
    next_cursor: str | None
