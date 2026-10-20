from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel


class StartAssistantChatRequest(SdkBaseModel):
    message: str
    """The first message to send to the assistant, exactly as a person would type it into the assistant on a new
    project."""

    auto_generate: bool = Field(default=False, alias="autoGenerate")
    """When true, the assistant picks the best workflow for the message and immediately starts generating, skipping the
    suggestion step. When the assistant message reaches ``succeeded``, its ``generation`` carries the workflow run to
    poll."""


class StartAssistantChatRequestDict(TypedDict):
    message: str
    auto_generate: NotRequired[bool]
