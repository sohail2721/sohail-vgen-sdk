from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemixProjectResponse(SdkBaseModel):
    """Returned when remix actions are accepted. Poll ``GET /v1/projects/{projectId}/remix-actions`` for status."""

    project_id: str = Field(alias="projectId")
    """Id of the edited project (e.g. ``vg_proj_...``; the duplicate when ``saveAsNewProject`` was true)."""

    project_url: str = Field(alias="projectUrl")
    """Deep link to open this project in the VideoGen web editor. Not required for an API-only integration: store
    ``projectId`` and use the Projects API (export, remix, metadata). Use ``projectUrl`` when a person should open the
    project in the app to review or edit it manually. The project is visible only to members of your team and any
    project collaborators, the same access model as a project created in the dashboard."""

    remix_action_ids: list[str] = Field(alias="remixActionIds")
    """Opaque remix action ids (e.g. ``vg_rmix_...``), one per requested action in order."""


class RemixProjectResponseDict(TypedDict):
    project_id: str
    project_url: str
    remix_action_ids: list[str]
