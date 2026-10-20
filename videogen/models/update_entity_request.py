from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class UpdateEntityRequest(SdkBaseModel):
    """At least one field must be provided."""

    name: OptionalNullable[str] = UNSET
    """New display name. Omit to leave unchanged."""

    description: OptionalNullable[str] = UNSET
    """New description. Omit to leave unchanged."""


class UpdateEntityRequestDict(TypedDict):
    name: NotRequired[str | None]
    description: NotRequired[str | None]
