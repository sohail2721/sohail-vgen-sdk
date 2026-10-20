from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class JobStatus(str, Enum):
    """Lifecycle status shared by every asynchronous job (tool executions, workflow runs, remix actions, project
    exports, and timeline interchange jobs). ``pending`` and ``running`` are in-progress; ``succeeded``, ``failed``, and
    ``cancelled`` are terminal."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"

    __str__ = str.__str__


JobStatusOrStr: TypeAlias = Annotated[JobStatus | str, open_enum_validator(JobStatus)]
