from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .aspect_ratio import AspectRatio, AspectRatioDict
from .enums.project_response_status import ProjectResponseStatusOrStr


class ProjectResponse(SdkBaseModel):
    """Simplified project metadata."""

    project_id: str = Field(alias="projectId")
    """Opaque project id (e.g. ``vg_proj_...``)."""

    assistant_id: str | None = Field(alias="assistantId")
    """Opaque id of this project's assistant conversation (e.g. ``vg_asst_...``). Use with the Assistant API to send
    follow-up messages or list the assistant's prior messages for this project. ``null`` for older projects created
    before assistant chats were attached at creation time."""

    title: str
    aspect_ratio: AspectRatio = Field(alias="aspectRatio")
    """Aspect ratio as a width:height pair (e.g. 16 and 9 for 16:9). Not pixel dimensions."""

    status: ProjectResponseStatusOrStr
    """High-level project status."""

    created_at: int = Field(alias="createdAt")
    """Seconds since epoch (Unix timestamp) when the project was created."""

    updated_at: int = Field(alias="updatedAt")
    """Seconds since epoch (Unix timestamp) when the project was last updated."""

    project_url: str = Field(alias="projectUrl")
    """Deep link to open this project in the VideoGen web editor. Not required for an API-only integration: store
    ``projectId`` and use the Projects API (export, remix, metadata). Use ``projectUrl`` when a person should open the
    project in the app to review or edit it manually. The project is visible only to members of your team and any
    project collaborators, the same access model as a project created in the dashboard."""


class ProjectResponseDict(TypedDict):
    project_id: str
    assistant_id: str | None
    title: str
    aspect_ratio: AspectRatioDict
    status: ProjectResponseStatusOrStr
    created_at: int
    updated_at: int
    project_url: str
