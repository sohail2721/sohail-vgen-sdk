from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileType(str, Enum):
    """File type. ``TEXT`` covers plain-text and editor-interchange documents; ``LOTTIE`` is a JSON animation."""

    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    PDF = "PDF"
    SLIDESHOW = "SLIDESHOW"
    TEXT = "TEXT"
    LOTTIE = "LOTTIE"

    __str__ = str.__str__


FileTypeOrStr: TypeAlias = Annotated[FileType | str, open_enum_validator(FileType)]
