from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimelineInterchangeMediaDelivery(str, Enum):
    """How the interchange document references media. ``REMOTE_URLS`` produces a single document that links to signed
    media URLs. ``BUNDLE`` produces a zip containing the document plus every referenced media file, referenced by
    relative path, for durable offline relinking."""

    REMOTE_URLS = "REMOTE_URLS"
    BUNDLE = "BUNDLE"

    __str__ = str.__str__


TimelineInterchangeMediaDeliveryOrStr: TypeAlias = Annotated[
    TimelineInterchangeMediaDelivery | str, open_enum_validator(TimelineInterchangeMediaDelivery)
]
