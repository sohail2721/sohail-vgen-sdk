from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ActOnAssistantActionResponse(SdkBaseModel):
    """Returned when a ``POST /v1/assistants/{assistantId}/actions/{actionId}`` call is accepted. Use ``messageId`` to
    poll the resulting assistant message."""

    message_id: str = Field(alias="messageId")
    """Opaque assistant message id for the assistant reply produced by acting on the action (e.g. ``vg_mesg_...``). Poll
    ``GET /v1/assistant-messages/{messageId}``."""


class ActOnAssistantActionResponseDict(TypedDict):
    message_id: str
