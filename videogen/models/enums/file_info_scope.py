from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileInfoScope(str, Enum):
    """File scope.

    - ``GLOBAL``: user-uploaded or standalone generated files that persist indefinitely.
    - ``PROJECT``: project-specific files (e.g. text-to-speech clips in a generated project).
    - ``EXPORT``: project exports.
    - ``TEMPORARY``: short-lived files guaranteed to be available for 24 hours, after which they may be archived at any
        time. Not analyzed (no description, transcript, or embedding).
    - ``ENTITY``: files attached to a reusable entity (e.g. a voice sample for an actor), shared across your team."""

    GLOBAL = "GLOBAL"
    PROJECT = "PROJECT"
    EXPORT = "EXPORT"
    TEMPORARY = "TEMPORARY"
    ENTITY = "ENTITY"

    __str__ = str.__str__


FileInfoScopeOrStr: TypeAlias = Annotated[FileInfoScope | str, open_enum_validator(FileInfoScope)]
