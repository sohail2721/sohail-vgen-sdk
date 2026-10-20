from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RemixAction(SdkBaseModel):
    """Set, replace, or remove the project's background music track."""

    type_: Literal["SET_BACKGROUND_MUSIC"] = Field(default="SET_BACKGROUND_MUSIC", alias="type")
    """Discriminator value: SET_BACKGROUND_MUSIC"""

    file_id: OptionalNullable[str] = Field(default=UNSET, alias="fileId")
    """File id of an uploaded audio file to use as background music (e.g. ``vg_file_...``). Upload it first via ``POST
    /v1/files/upload``. Pass ``null`` to remove the existing background music."""

    volume: OptionalNullable[float] = UNSET
    """Music volume from 0 (silent) to 1 (full). Omit or pass ``null`` to keep the current volume."""


class RemixActionDict(TypedDict):
    type_: Literal["SET_BACKGROUND_MUSIC"]
    file_id: NotRequired[str | None]
    volume: NotRequired[float | None]
