from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .assistant_message_attachment import AssistantMessageAttachment, AssistantMessageAttachmentDict
from .enums.assistant_message_status import AssistantMessageStatusOrStr


class AssistantMessage(SdkBaseModel):
    """A user-authored message in an assistant chat."""

    role: Literal["user"] = "user"
    """Discriminator value: user"""

    message_id: str = Field(alias="messageId")
    """Opaque assistant message id (e.g. ``vg_mesg_...``)."""

    status: AssistantMessageStatusOrStr
    """Lifecycle status of an assistant chat message. ``pending`` and ``running`` are in-progress; ``succeeded``,
    ``failed``, and ``cancelled`` are terminal."""

    content: str
    """The user's message text."""

    attachments: list[AssistantMessageAttachment]
    """Files attached to this message."""

    created_at: int = Field(alias="createdAt")
    """Seconds since epoch (Unix timestamp) when the message was created."""


class AssistantMessageDict(TypedDict):
    role: Literal["user"]
    message_id: str
    status: AssistantMessageStatusOrStr
    content: str
    attachments: list[AssistantMessageAttachmentDict]
    created_at: int
