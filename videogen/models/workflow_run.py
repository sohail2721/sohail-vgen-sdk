from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .api_error_model import ApiErrorModel, ApiErrorModelDict
from .enums.job_status import JobStatusOrStr
from .enums.workflow_type import WorkflowTypeOrStr


class WorkflowRun(SdkBaseModel):
    workflow_run_id: str = Field(alias="workflowRunId")
    """Opaque workflow run id."""

    status: JobStatusOrStr
    """Lifecycle status shared by every asynchronous job (tool executions, workflow runs, remix actions, project
    exports, and timeline interchange jobs). ``pending`` and ``running`` are in-progress; ``succeeded``, ``failed``, and
    ``cancelled`` are terminal."""

    workflow_type: WorkflowTypeOrStr = Field(alias="workflowType")
    """Workflow type identifier."""

    progress_percentage: float = Field(alias="progressPercentage")
    """Completion progress for the current attempt (0-100). Always ``100`` when ``status`` is ``succeeded``."""

    attempt_index: int = Field(alias="attemptIndex")
    """Zero-based index of the current or most recent execution attempt."""

    project_id: str = Field(alias="projectId")
    """Id of the project created for this workflow run (e.g. ``vg_proj_...``)."""

    project_url: str = Field(alias="projectUrl")
    """Deep link to open this project in the VideoGen web editor. Not required for an API-only integration: store
    ``projectId`` and use the Projects API (export, remix, metadata). Use ``projectUrl`` when a person should open the
    project in the app to review or edit it manually. The project is visible only to members of your team and any
    project collaborators, the same access model as a project created in the dashboard."""

    error: ApiErrorModel | None
    """Error details. Always present as a field; ``null`` unless ``status`` is ``failed``."""


class WorkflowRunDict(TypedDict):
    workflow_run_id: str
    status: JobStatusOrStr
    workflow_type: WorkflowTypeOrStr
    progress_percentage: float
    attempt_index: int
    project_id: str
    project_url: str
    error: ApiErrorModelDict | None
