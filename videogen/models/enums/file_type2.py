from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileType2(str, Enum):
    """The type of file to upload. Optional; when omitted, the type is inferred after upload processing completes."""

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    PDF = "PDF"
    SLIDESHOW = "SLIDESHOW"
    TEXT = "TEXT"
    LOTTIE = "LOTTIE"

    __str__ = str.__str__


FileType2OrStr: TypeAlias = Annotated[FileType2 | str, open_enum_validator(FileType2)]
