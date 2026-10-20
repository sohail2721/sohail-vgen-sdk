from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WorkflowCaptionStyleFontWeight(str, Enum):
    """Numeric font weight (400 = regular, 700 = bold)."""

    _100 = "100"
    _200 = "200"
    _300 = "300"
    _400 = "400"
    _500 = "500"
    _600 = "600"
    _700 = "700"
    _800 = "800"
    _900 = "900"

    __str__ = str.__str__


WorkflowCaptionStyleFontWeightOrStr: TypeAlias = Annotated[
    WorkflowCaptionStyleFontWeight | str, open_enum_validator(WorkflowCaptionStyleFontWeight)
]
