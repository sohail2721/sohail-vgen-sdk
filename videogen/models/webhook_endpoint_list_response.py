from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .webhook_endpoint import WebhookEndpoint, WebhookEndpointDict


class WebhookEndpointListResponse(SdkBaseModel):
    endpoints: list[WebhookEndpoint]
    has_more: bool = Field(alias="hasMore")
    """When true, there are more endpoints available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the
    next page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class WebhookEndpointListResponseDict(TypedDict):
    endpoints: list[WebhookEndpointDict]
    has_more: bool
    next_cursor: str | None
