from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .assistant_action_detail1 import AssistantActionDetail1, AssistantActionDetail1Dict
from .enums.assistant_action_kind import AssistantActionKindOrStr


class AssistantAction(SdkBaseModel):
    """An actionable widget the assistant offered on this turn. Act on it with ``POST
    /v1/assistants/{assistantId}/actions/{actionId}`` unless ``requiresApp`` is true."""

    action_id: str = Field(alias="actionId")
    """Opaque id to pass to the act-on-action endpoint."""

    kind: AssistantActionKindOrStr
    """Normalized category of an actionable widget the assistant offered. ``APPROVE_PLAN`` accepts a proposed generation
    plan; ``APPLY_EDIT`` applies a proposed edit (e.g. a rewritten script); ``RUN_TOOL`` runs an inline tool;
    ``GENERATE`` starts building the video; ``OPEN_IN_APP`` requires the full web app — open the assistant's
    ``projectUrl`` instead of acting via the API."""

    label: str
    """Human-readable label describing what acting on this will do."""

    requires_app: bool = Field(alias="requiresApp")
    """When true, this action can only be completed in the web app; open the assistant's ``projectUrl`` instead of
    calling the API."""

    detail: Optional[AssistantActionDetail1] = UNSET
    """Optional extra data for rendering this action inline without opening the app."""


class AssistantActionDict(TypedDict):
    action_id: str
    kind: AssistantActionKindOrStr
    label: str
    requires_app: bool
    detail: NotRequired[AssistantActionDetail1Dict]
