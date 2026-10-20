from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemixAction5(SdkBaseModel):
    """Apply a Ken Burns zoom to every eligible still image in the project, including uploaded images. Replaces any
    existing still-image effect on those assets. If the project has no eligible stills, the action is skipped and
    completes successfully without changing anything."""

    type_: Literal["ADD_ZOOM"] = Field(default="ADD_ZOOM", alias="type")
    """Discriminator value: ADD_ZOOM"""


class RemixAction5Dict(TypedDict):
    type_: Literal["ADD_ZOOM"]
