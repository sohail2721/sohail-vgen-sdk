from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.remix_action_discriminator_mapping_set_logo_position import (
    RemixActionDiscriminatorMappingSetLogoPositionOrStr,
)


class RemixAction1(SdkBaseModel):
    """Set, replace, or remove the logo overlay."""

    type_: Literal["SET_LOGO"] = Field(default="SET_LOGO", alias="type")
    """Discriminator value: SET_LOGO"""

    file_id: OptionalNullable[str] = Field(default=UNSET, alias="fileId")
    """File id of an uploaded image to overlay as a logo (e.g. ``vg_file_...``). Upload it first via ``POST
    /v1/files/upload``. Pass ``null`` to remove the existing logo."""

    position: Optional[RemixActionDiscriminatorMappingSetLogoPositionOrStr] = UNSET
    """Position the logo is anchored to. Omit or pass ``null`` to keep the current position."""

    size_percent: OptionalNullable[float] = Field(default=UNSET, alias="sizePercent")
    """Logo width as a percentage of the video width. Omit or pass ``null`` to keep the current size."""


class RemixAction1Dict(TypedDict):
    type_: Literal["SET_LOGO"]
    file_id: NotRequired[str | None]
    position: NotRequired[RemixActionDiscriminatorMappingSetLogoPositionOrStr]
    size_percent: NotRequired[float | None]
