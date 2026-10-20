from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .api_error_model import ApiErrorModel, ApiErrorModelDict
from .assistant_action import AssistantAction, AssistantActionDict
from .assistant_message_attachment import AssistantMessageAttachment, AssistantMessageAttachmentDict
from .assistant_workflow_suggestion import AssistantWorkflowSuggestion, AssistantWorkflowSuggestionDict
from .enums.assistant_message_status import AssistantMessageStatusOrStr
from .start_workflow_run_response import StartWorkflowRunResponse, StartWorkflowRunResponseDict


class AssistantMessage1(SdkBaseModel):
    """An assistant-authored message in an assistant chat, including any suggestions or actions it offered."""

    role: Literal["assistant"] = "assistant"
    """Discriminator value: assistant"""

    message_id: str = Field(alias="messageId")
    """Opaque assistant message id (e.g. ``vg_mesg_...``)."""

    status: AssistantMessageStatusOrStr
    """Lifecycle status of an assistant chat message. ``pending`` and ``running`` are in-progress; ``succeeded``,
    ``failed``, and ``cancelled`` are terminal."""

    content: str | None
    """The assistant's text reply. ``null`` while ``status`` is ``pending`` or ``running``; may be empty when the
    assistant only offered widgets."""

    attachments: list[AssistantMessageAttachment]
    """Files attached to this message."""

    workflow_suggestions: list[AssistantWorkflowSuggestion] = Field(alias="workflowSuggestions")
    """Workflow starting points the assistant suggested on this message. Empty when none were offered."""

    actions: list[AssistantAction]
    """Actionable widgets the assistant offered on this message (plans, edits, tools, generate). Empty when none were
    offered."""

    generation: StartWorkflowRunResponse | None
    """Present when this message kicked off a workflow run (via ``autoGenerate`` on start, or acting on a workflow
    suggestion): the workflow run to poll via ``GET /v1/workflows/runs/{workflowRunId}``."""

    error: ApiErrorModel | None
    """Error details. ``null`` unless ``status`` is ``failed``."""

    created_at: int = Field(alias="createdAt")
    """Seconds since epoch (Unix timestamp) when the message was created."""


class AssistantMessage1Dict(TypedDict):
    role: Literal["assistant"]
    message_id: str
    status: AssistantMessageStatusOrStr
    content: str | None
    attachments: list[AssistantMessageAttachmentDict]
    workflow_suggestions: list[AssistantWorkflowSuggestionDict]
    actions: list[AssistantActionDict]
    generation: StartWorkflowRunResponseDict | None
    error: ApiErrorModelDict | None
    created_at: int
