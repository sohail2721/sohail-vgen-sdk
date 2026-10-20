from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .unions.remix_action15 import RemixAction15, RemixAction15Dict


class RemixProjectRequest(SdkBaseModel):
    remix_actions: list[RemixAction15] = Field(alias="remixActions")
    """Ordered list of edits to apply. Each runs asynchronously as its own remix action. Must contain at least one
    action."""

    save_as_new_project: Optional[bool] = Field(default=UNSET, alias="saveAsNewProject")
    """When true, the project is duplicated first and the edits are applied to the copy, leaving the original untouched.
    The response's ``projectId`` is the copy. Defaults to false (edits the project in place)."""


class RemixProjectRequestDict(TypedDict):
    remix_actions: list[RemixAction15Dict]
    save_as_new_project: NotRequired[bool]
