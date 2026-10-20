from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExportProjectQuality(str, Enum):
    """Vertical resolution tier for the rendered MP4."""

    STANDARD = "STANDARD"
    HIGH = "HIGH"
    FULL_HIGH = "FULL_HIGH"
    ULTRA_HIGH = "ULTRA_HIGH"

    __str__ = str.__str__


ExportProjectQualityOrStr: TypeAlias = Annotated[ExportProjectQuality | str, open_enum_validator(ExportProjectQuality)]
