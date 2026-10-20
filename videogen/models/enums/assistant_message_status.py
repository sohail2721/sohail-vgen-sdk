from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class AssistantMessageStatus(str, Enum):
    """Lifecycle status of an assistant chat message. ``pending`` and ``running`` are in-progress; ``succeeded``,
    ``failed``, and ``cancelled`` are terminal."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"

    __str__ = str.__str__


AssistantMessageStatusOrStr: TypeAlias = Annotated[
    AssistantMessageStatus | str, open_enum_validator(AssistantMessageStatus)
]
