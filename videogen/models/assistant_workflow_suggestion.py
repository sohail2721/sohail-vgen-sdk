from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.workflow_type1 import WorkflowType1OrStr


class AssistantWorkflowSuggestion(SdkBaseModel):
    """A starting-point workflow the assistant suggests for the conversation. Act on it with ``POST
    /v1/assistants/{assistantId}/actions/{actionId}`` to select the workflow and continue."""

    action_id: str = Field(alias="actionId")
    """Opaque id to pass to the act-on-action endpoint to select this workflow."""

    workflow_type: WorkflowType1OrStr = Field(alias="workflowType")
    """Identifier of the suggested workflow."""

    title: str
    """Short human-readable name of the suggested workflow."""

    description: str
    """One-line explanation of what this workflow will do."""


class AssistantWorkflowSuggestionDict(TypedDict):
    action_id: str
    workflow_type: WorkflowType1OrStr
    title: str
    description: str
