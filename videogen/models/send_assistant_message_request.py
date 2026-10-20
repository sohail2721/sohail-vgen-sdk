from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class SendAssistantMessageRequest(SdkBaseModel):
    message: str
    """The message to send to the assistant in this project chat."""


class SendAssistantMessageRequestDict(TypedDict):
    message: str
