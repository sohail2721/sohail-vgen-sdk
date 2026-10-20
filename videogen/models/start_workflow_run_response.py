from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StartWorkflowRunResponse(SdkBaseModel):
    """Returned when a workflow run is accepted. Poll ``GET /v1/workflows/runs/{workflowRunId}`` or subscribe to
    webhooks for completion."""

    workflow_run_id: str = Field(alias="workflowRunId")
    """Opaque workflow run id (e.g. ``vg_work_...``)."""

    project_id: str = Field(alias="projectId")
    """Id of the project created for this workflow run (e.g. ``vg_proj_...``)."""

    project_url: str = Field(alias="projectUrl")
    """Deep link to open this project in the VideoGen web editor. Not required for an API-only integration: store
    ``projectId`` and use the Projects API (export, remix, metadata). Use ``projectUrl`` when a person should open the
    project in the app to review or edit it manually. The project is visible only to members of your team and any
    project collaborators, the same access model as a project created in the dashboard."""

    remix_action_ids: list[str] = Field(alias="remixActionIds")
    """Opaque remix action ids (e.g. ``vg_rmix_...``), one per ``remixActions`` entry in request order. Empty when no
    remix actions were requested. Each runs after the video is built; poll ``GET
    /v1/projects/{projectId}/remix-actions``."""


class StartWorkflowRunResponseDict(TypedDict):
    workflow_run_id: str
    project_id: str
    project_url: str
    remix_action_ids: list[str]
