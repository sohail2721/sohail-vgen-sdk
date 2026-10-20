from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .api_error_model import ApiErrorModel, ApiErrorModelDict
from .enums.job_status import JobStatusOrStr
from .tool_success_result import ToolSuccessResult, ToolSuccessResultDict


class ExecutedTool(SdkBaseModel):
    tool_execution_id: str = Field(alias="toolExecutionId")
    """Execution id matching the original request."""

    status: JobStatusOrStr
    """Lifecycle status shared by every asynchronous job (tool executions, workflow runs, remix actions, project
    exports, and timeline interchange jobs). ``pending`` and ``running`` are in-progress; ``succeeded``, ``failed``, and
    ``cancelled`` are terminal."""

    tool_type: str = Field(alias="toolType")
    """Tool name (e.g. ``GENERATE_IMAGE``, ``TEXT_TO_SPEECH``)."""

    progress_percentage: float = Field(alias="progressPercentage")
    """Completion progress for the current attempt (0-100). Always ``100`` when ``status`` is ``succeeded``."""

    attempt_index: int = Field(alias="attemptIndex")
    """Zero-based index of the current or most recent execution attempt."""

    results: list[ToolSuccessResult]
    """One entry per generated result. Always present; empty until ``status`` is ``succeeded``, then one entry per
    generated file (each with signed URLs and a hydrated ``file``)."""

    error: ApiErrorModel | None
    """Error details. Always present; ``null`` unless ``status`` is ``failed``."""


class ExecutedToolDict(TypedDict):
    tool_execution_id: str
    status: JobStatusOrStr
    tool_type: str
    progress_percentage: float
    attempt_index: int
    results: list[ToolSuccessResultDict]
    error: ApiErrorModelDict | None
