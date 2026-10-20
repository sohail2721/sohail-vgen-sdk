from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class StartAssistantChatResponse(SdkBaseModel):
    """Returned when a ``POST /v1/assistants`` call is accepted. Poll ``messageId`` for the pending assistant reply;
    keep ``assistantId`` / ``projectId`` to continue the chat and address the project."""

    message_id: str = Field(alias="messageId")
    """Opaque assistant message id for the pending assistant reply (e.g. ``vg_mesg_...``). Poll ``GET
    /v1/assistant-messages/{messageId}``."""

    assistant_id: str = Field(alias="assistantId")
    """Opaque assistant chat id (e.g. ``vg_asst_...``). Pass to ``GET /v1/assistants/{assistantId}`` and follow-up
    message/action calls."""

    project_id: str = Field(alias="projectId")
    """Opaque project id for the new chat (e.g. ``vg_proj_...``)."""

    project_url: str = Field(alias="projectUrl")
    """Deep link to open this project in the VideoGen web app."""


class StartAssistantChatResponseDict(TypedDict):
    message_id: str
    assistant_id: str
    project_id: str
    project_url: str
