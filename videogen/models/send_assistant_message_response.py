from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SendAssistantMessageResponse(SdkBaseModel):
    """Returned when a ``POST /v1/assistants/{assistantId}/messages`` call is accepted. Use ``messageId`` to poll the
    pending assistant reply."""

    message_id: str = Field(alias="messageId")
    """Opaque assistant message id for the pending assistant reply (e.g. ``vg_mesg_...``). Poll ``GET
    /v1/assistant-messages/{messageId}``."""


class SendAssistantMessageResponseDict(TypedDict):
    message_id: str
