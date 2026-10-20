from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ExportDeliveryDestinationType(str, Enum):
    """Where to deliver the export within the connected integration."""

    SLACK_CHANNEL = "SLACK_CHANNEL"
    GOOGLE_DRIVE_FOLDER = "GOOGLE_DRIVE_FOLDER"

    __str__ = str.__str__


ExportDeliveryDestinationTypeOrStr: TypeAlias = Annotated[
    ExportDeliveryDestinationType | str, open_enum_validator(ExportDeliveryDestinationType)
]
