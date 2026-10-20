from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.workflow_caption_style_font_weight import WorkflowCaptionStyleFontWeightOrStr
from .enums.workflow_caption_style_text_justification import WorkflowCaptionStyleTextJustificationOrStr
from .enums.workflow_caption_style_vertical_alignment import WorkflowCaptionStyleVerticalAlignmentOrStr
from .workflow_caption_background_style import WorkflowCaptionBackgroundStyle, WorkflowCaptionBackgroundStyleDict
from .workflow_rgb_color import WorkflowRgbColor, WorkflowRgbColorDict


class WorkflowCaptionStyle(SdkBaseModel):
    """Caption styling. Any omitted field falls back to the VideoGen default caption style. Provide an empty object
    (``{}``) to keep the default style but ensure captions are shown. Pass ``null`` for the whole ``captionStyle`` field
    to hide captions entirely."""

    font_name: Optional[str] = Field(default=UNSET, alias="fontName")
    """Font family name."""

    font_size: Optional[float] = Field(default=UNSET, alias="fontSize")
    """Font size in pixels at 1080p. Must be greater than 0."""

    font_weight: Optional[WorkflowCaptionStyleFontWeightOrStr] = Field(default=UNSET, alias="fontWeight")
    """Numeric font weight (400 = regular, 700 = bold)."""

    text_color: Optional[WorkflowRgbColor] = Field(default=UNSET, alias="textColor")
    """An RGB color. Each channel is an integer from 0 to 255."""

    text_justification: Optional[WorkflowCaptionStyleTextJustificationOrStr] = Field(
        default=UNSET, alias="textJustification"
    )
    vertical_alignment: Optional[WorkflowCaptionStyleVerticalAlignmentOrStr] = Field(
        default=UNSET, alias="verticalAlignment"
    )
    """Vertical position of the caption block in the frame."""

    stroke_color: OptionalNullable[WorkflowRgbColor] = Field(default=UNSET, alias="strokeColor")
    """Outline color around glyphs, or null for no outline."""

    stroke_weight: Optional[float] = Field(default=UNSET, alias="strokeWeight")
    """Outline thickness in pixels. 0 disables the outline."""

    background_style: OptionalNullable[WorkflowCaptionBackgroundStyle] = Field(default=UNSET, alias="backgroundStyle")
    """Background drawn behind the text, or null for no background."""

    spoken_text_color: OptionalNullable[WorkflowRgbColor] = Field(default=UNSET, alias="spokenTextColor")
    """Color applied to the currently spoken word for karaoke-style highlighting, or null to keep the base text
    color."""

    spoken_text_stroke_color: OptionalNullable[WorkflowRgbColor] = Field(default=UNSET, alias="spokenTextStrokeColor")
    """Outline color applied to the currently spoken word, or null."""

    persist_spoken_text_color: Optional[bool] = Field(default=UNSET, alias="persistSpokenTextColor")
    """When true, a word keeps the spoken-text color after it has been spoken instead of reverting."""


class WorkflowCaptionStyleDict(TypedDict):
    font_name: NotRequired[str]
    font_size: NotRequired[float]
    font_weight: NotRequired[WorkflowCaptionStyleFontWeightOrStr]
    text_color: NotRequired[WorkflowRgbColorDict]
    text_justification: NotRequired[WorkflowCaptionStyleTextJustificationOrStr]
    vertical_alignment: NotRequired[WorkflowCaptionStyleVerticalAlignmentOrStr]
    stroke_color: NotRequired[WorkflowRgbColorDict | None]
    stroke_weight: NotRequired[float]
    background_style: NotRequired[WorkflowCaptionBackgroundStyleDict | None]
    spoken_text_color: NotRequired[WorkflowRgbColorDict | None]
    spoken_text_stroke_color: NotRequired[WorkflowRgbColorDict | None]
    persist_spoken_text_color: NotRequired[bool]
