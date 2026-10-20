from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ErrorRequirement(SdkBaseModel):
    """What is needed to resolve an error, when it can be fixed by fulfilling a specific requirement (e.g. purchasing an
    add-on or upgrading the plan)."""

    type_: str = Field(alias="type")
    """Machine-readable requirement type in snake_case (e.g. ``purchase_add_on``, ``upgrade_plan``)."""

    details: Optional[dict[str, str]] = UNSET
    """Key-value pairs with requirement-specific context (e.g. the add-on id to purchase)."""


class ErrorRequirementDict(TypedDict):
    type_: str
    details: NotRequired[dict[str, str]]
