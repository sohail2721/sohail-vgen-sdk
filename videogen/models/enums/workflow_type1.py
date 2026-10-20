from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkflowType1(str, Enum):
    """Identifier of the suggested workflow."""

    SCRIPT_TO_VIDEO = "SCRIPT_TO_VIDEO"
    VOICEOVER_TO_VIDEO = "VOICEOVER_TO_VIDEO"
    SLIDESHOW_TO_VIDEO = "SLIDESHOW_TO_VIDEO"
    STORYBOARD_TO_VIDEO = "STORYBOARD_TO_VIDEO"
    PROMPT_TO_VIDEO_CLIP = "PROMPT_TO_VIDEO_CLIP"
    CREATIVE_BRIEF_TO_VIDEO = "CREATIVE_BRIEF_TO_VIDEO"

    __str__ = str.__str__


WorkflowType1OrStr: TypeAlias = Annotated[WorkflowType1 | str, open_enum_validator(WorkflowType1)]
