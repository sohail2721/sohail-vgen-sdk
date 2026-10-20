from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TimelineInterchangeFormat(str, Enum):
    """Editor interchange document format. ``FCPXML`` is Final Cut Pro (also imported by DaVinci Resolve and others).
    ``PREMIERE_XML`` is the Final Cut 7 ``xmeml`` XML that Adobe Premiere Pro imports natively. ``OTIO`` is
    OpenTimelineIO, the vendor-neutral format. ``SRT`` is a SubRip caption sidecar."""

    FCPXML = "FCPXML"
    PREMIERE_XML = "PREMIERE_XML"
    OTIO = "OTIO"
    SRT = "SRT"

    __str__ = str.__str__


TimelineInterchangeFormatOrStr: TypeAlias = Annotated[
    TimelineInterchangeFormat | str, open_enum_validator(TimelineInterchangeFormat)
]
