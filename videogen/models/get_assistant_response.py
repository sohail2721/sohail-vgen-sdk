from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .unions.assistant_message2 import AssistantMessage2, AssistantMessage2Dict


class GetAssistantResponse(SdkBaseModel):
    """An assistant chat and every message it currently contains."""

    assistant_id: str = Field(alias="assistantId")
    """Opaque assistant chat id (e.g. ``vg_asst_...``)."""

    project_id: str = Field(alias="projectId")
    """Opaque project id of the project this chat belongs to (e.g. ``vg_proj_...``)."""

    project_url: str = Field(alias="projectUrl")
    """Deep link to open this chat's project in the VideoGen web app. Visible only to members of your team and project
    collaborators."""

    messages: list[AssistantMessage2]
    """Every message in the chat in chronological order (oldest first)."""


class GetAssistantResponseDict(TypedDict):
    assistant_id: str
    project_id: str
    project_url: str
    messages: list[AssistantMessage2Dict]
