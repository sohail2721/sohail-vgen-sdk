from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.remix_transition_style import RemixTransitionStyleOrStr


class RemixAction4(SdkBaseModel):
    """Stamp transitions across the project. Not per-boundary: each field you set is applied uniformly to every boundary
    in that scope, replacing any transition already there. Set the transition between sections, between base-layer
    assets, or both; omit or pass ``null`` for a scope to leave its transitions untouched."""

    type_: Literal["ADD_TRANSITIONS"] = Field(default="ADD_TRANSITIONS", alias="type")
    """Discriminator value: ADD_TRANSITIONS"""

    section_transition: OptionalNullable[RemixTransitionStyleOrStr] = Field(default=UNSET, alias="sectionTransition")
    """Transition applied at every boundary between sections, replacing any existing section transitions. Omit or pass
    ``null`` to leave section transitions untouched."""

    asset_transition: OptionalNullable[RemixTransitionStyleOrStr] = Field(default=UNSET, alias="assetTransition")
    """Transition applied at every boundary between base-layer assets within sections, replacing any existing asset
    transitions. Omit or pass ``null`` to leave asset transitions untouched."""


class RemixAction4Dict(TypedDict):
    type_: Literal["ADD_TRANSITIONS"]
    section_transition: NotRequired[RemixTransitionStyleOrStr | None]
    asset_transition: NotRequired[RemixTransitionStyleOrStr | None]
