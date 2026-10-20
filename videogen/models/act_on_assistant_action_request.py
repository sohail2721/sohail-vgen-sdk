from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import SdkBaseModel
from .enums.act_on_assistant_action_request_decision import (
    ActOnAssistantActionRequestDecision,
    ActOnAssistantActionRequestDecisionOrStr,
)


class ActOnAssistantActionRequest(SdkBaseModel):
    decision: ActOnAssistantActionRequestDecisionOrStr = ActOnAssistantActionRequestDecision.APPROVE
    """Whether to approve (apply) or reject the action. Defaults to ``APPROVE``."""


class ActOnAssistantActionRequestDict(TypedDict):
    decision: NotRequired[ActOnAssistantActionRequestDecisionOrStr]
