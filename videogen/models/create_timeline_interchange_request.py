from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.timeline_interchange_format import TimelineInterchangeFormatOrStr
from .enums.timeline_interchange_media_delivery import TimelineInterchangeMediaDeliveryOrStr


class CreateTimelineInterchangeRequest(SdkBaseModel):
    format: Optional[TimelineInterchangeFormatOrStr] = UNSET
    """Editor interchange document format. ``FCPXML`` is Final Cut Pro (also imported by DaVinci Resolve and others).
    ``PREMIERE_XML`` is the Final Cut 7 ``xmeml`` XML that Adobe Premiere Pro imports natively. ``OTIO`` is
    OpenTimelineIO, the vendor-neutral format. ``SRT`` is a SubRip caption sidecar."""

    media_delivery: Optional[TimelineInterchangeMediaDeliveryOrStr] = Field(default=UNSET, alias="mediaDelivery")
    """How the interchange document references media. ``REMOTE_URLS`` produces a single document that links to signed
    media URLs. ``BUNDLE`` produces a zip containing the document plus every referenced media file, referenced by
    relative path, for durable offline relinking."""


class CreateTimelineInterchangeRequestDict(TypedDict):
    format: NotRequired[TimelineInterchangeFormatOrStr]
    media_delivery: NotRequired[TimelineInterchangeMediaDeliveryOrStr]
