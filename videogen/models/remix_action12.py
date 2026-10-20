from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemixAction12(SdkBaseModel):
    """Replace every stock (library) visual in the project with a fresh alternative from the same search, replacing each
    in place. Runs asynchronously: each stock asset's original search is re-run, excluding the currently-shown result.
    If the project has no shuffleable stock visuals, the action is skipped and completes successfully without changing
    anything."""

    type_: Literal["SHUFFLE_STOCK_VISUALS"] = Field(default="SHUFFLE_STOCK_VISUALS", alias="type")
    """Discriminator value: SHUFFLE_STOCK_VISUALS"""


class RemixAction12Dict(TypedDict):
    type_: Literal["SHUFFLE_STOCK_VISUALS"]
