from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class RemixAction3(SdkBaseModel):
    """Hide captions on every captionable section."""

    type_: Literal["DISABLE_CAPTIONS"] = Field(default="DISABLE_CAPTIONS", alias="type")
    """Discriminator value: DISABLE_CAPTIONS"""


class RemixAction3Dict(TypedDict):
    type_: Literal["DISABLE_CAPTIONS"]
