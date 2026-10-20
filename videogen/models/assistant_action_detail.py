from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AssistantActionDetail(SdkBaseModel):
    """Extra data for rendering this action inline (in a chat surface or integration) without opening the web app.
    Fields are populated only when relevant to the action's kind; all are optional."""

    summary: OptionalNullable[str] = UNSET
    """Human-readable summary of the proposed plan or edit (for ``APPROVE_PLAN`` and ``APPLY_EDIT`` actions)."""

    credits_remaining: OptionalNullable[int] = Field(default=UNSET, alias="creditsRemaining")
    """Credits currently remaining on your team (for the usage/credits widget). A whole number of credits."""

    estimated_credits: OptionalNullable[int] = Field(default=UNSET, alias="estimatedCredits")
    """Estimated credit cost of the current workflow (for the cost-estimate widget). A whole number of credits."""


class AssistantActionDetailDict(TypedDict):
    summary: NotRequired[str | None]
    credits_remaining: NotRequired[int | None]
    estimated_credits: NotRequired[int | None]
