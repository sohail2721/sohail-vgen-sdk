from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileType1(str, Enum):
    """File type."""

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    PDF = "PDF"
    SLIDESHOW = "SLIDESHOW"
    TEXT = "TEXT"
    LOTTIE = "LOTTIE"

    __str__ = str.__str__


FileType1OrStr: TypeAlias = Annotated[FileType1 | str, open_enum_validator(FileType1)]
