from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.webhook_event_name import WebhookEventNameOrStr


class CreateWebhookEndpointRequest(SdkBaseModel):
    url: str
    """HTTPS URL that will receive webhook POST requests."""

    description: OptionalNullable[str] = UNSET
    events: list[WebhookEventNameOrStr]
    """Webhook event names to subscribe to. Must contain at least one event."""


class CreateWebhookEndpointRequestDict(TypedDict):
    url: str
    description: NotRequired[str | None]
    events: list[WebhookEventNameOrStr]
