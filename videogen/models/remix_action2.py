from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .workflow_caption_style import WorkflowCaptionStyle, WorkflowCaptionStyleDict


class RemixAction2(SdkBaseModel):
    """Show captions on every captionable section. Optionally override the project caption style."""

    type_: Literal["ENABLE_CAPTIONS"] = Field(default="ENABLE_CAPTIONS", alias="type")
    """Discriminator value: ENABLE_CAPTIONS"""

    caption_style: OptionalNullable[WorkflowCaptionStyle] = Field(default=UNSET, alias="captionStyle")
    """Caption styling to apply. Omit or pass ``null`` to show captions with the current style. Any provided field
    overrides that field; omitted fields keep their current value."""


class RemixAction2Dict(TypedDict):
    type_: Literal["ENABLE_CAPTIONS"]
    caption_style: NotRequired[WorkflowCaptionStyleDict | None]
