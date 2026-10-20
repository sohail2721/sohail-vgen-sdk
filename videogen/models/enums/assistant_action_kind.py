from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssistantActionKind(str, Enum):
    """Normalized category of an actionable widget the assistant offered. ``APPROVE_PLAN`` accepts a proposed generation
    plan; ``APPLY_EDIT`` applies a proposed edit (e.g. a rewritten script); ``RUN_TOOL`` runs an inline tool;
    ``GENERATE`` starts building the video; ``OPEN_IN_APP`` requires the full web app — open the assistant's
    ``projectUrl`` instead of acting via the API."""

    APPROVE_PLAN = "APPROVE_PLAN"
    APPLY_EDIT = "APPLY_EDIT"
    RUN_TOOL = "RUN_TOOL"
    GENERATE = "GENERATE"
    OPEN_IN_APP = "OPEN_IN_APP"

    __str__ = str.__str__


AssistantActionKindOrStr: TypeAlias = Annotated[AssistantActionKind | str, open_enum_validator(AssistantActionKind)]
