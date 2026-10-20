from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkflowCaptionBackgroundStyleType(str, Enum):
    """RECT draws one rectangle behind the whole line; WRAPPED hugs the text; WORD_BY_WORD draws a box per word."""

    RECT = "RECT"
    WRAPPED = "WRAPPED"
    WORD_BY_WORD = "WORD_BY_WORD"

    __str__ = str.__str__


WorkflowCaptionBackgroundStyleTypeOrStr: TypeAlias = Annotated[
    WorkflowCaptionBackgroundStyleType | str, open_enum_validator(WorkflowCaptionBackgroundStyleType)
]
