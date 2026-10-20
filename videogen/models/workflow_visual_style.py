from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.workflow_visual_style_type import WorkflowVisualStyleTypeOrStr


class WorkflowVisualStyle(SdkBaseModel):
    """Visual style for the generated b-roll."""

    type_: WorkflowVisualStyleTypeOrStr = Field(alias="type")
    """STOCK pulls stock footage and images. AI_IMAGE generates a styled image for each section. Pass ``entityId`` to
    match a saved visual-style entity, or ``aiStyle`` for a free-form look."""

    ai_style: Optional[str] = Field(default=UNSET, alias="aiStyle")
    """Only applies when type is AI_IMAGE and ``entityId`` is omitted. A free-form description of the look applied to
    every generated image (e.g. ``vintage 1970s film photography, warm grain``). See the AI styles reference for example
    descriptions of the app's default styles. Required when type is AI_IMAGE and ``entityId`` is omitted."""

    entity_id: Optional[str] = Field(default=UNSET, alias="entityId")
    """Only applies when type is AI_IMAGE. The id of a VISUAL_STYLE entity (e.g. ``vg_enti_...``) whose reference images
    guide every generated image. When set, generated images match that entity instead of ``aiStyle``."""

    restyle_featured_b_roll_with_ai_style: bool = Field(default=True, alias="restyleFeaturedBRollWithAiStyle")
    """Only applies when type is AI_IMAGE. When true, featured b-roll images you provide are re-rendered in the chosen
    style so they match the generated look (no effect on featured b-roll videos). Defaults to true."""


class WorkflowVisualStyleDict(TypedDict):
    type_: WorkflowVisualStyleTypeOrStr
    ai_style: NotRequired[str]
    entity_id: NotRequired[str]
    restyle_featured_b_roll_with_ai_style: NotRequired[bool]
