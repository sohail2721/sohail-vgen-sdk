from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileSourceStatus(str, Enum):
    """``pending``: asset is still processing or has not been hydrated yet. ``ready``: signed URL is available.
    ``failed``: rendition generation failed. ``skipped``: rendition does not apply to this file type (e.g. thumbnail for
    audio)."""

    PENDING = "pending"
    READY = "ready"
    FAILED = "failed"
    SKIPPED = "skipped"

    __str__ = str.__str__


FileSourceStatusOrStr: TypeAlias = Annotated[FileSourceStatus | str, open_enum_validator(FileSourceStatus)]
