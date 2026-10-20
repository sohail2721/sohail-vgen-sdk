from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.webhook_event_name import WebhookEventNameOrStr


class WebhookEndpoint(SdkBaseModel):
    endpoint_id: str = Field(alias="endpointId")
    """Webhook endpoint id (e.g. ``ep_...``)."""

    url: str
    events: list[WebhookEventNameOrStr]
    description: OptionalNullable[str] = UNSET
    created_at: int = Field(alias="createdAt")
    """Seconds since epoch (Unix timestamp) when the endpoint was created."""

    signing_secret: Optional[str] = Field(default=UNSET, alias="signingSecret")
    """HMAC secret for verifying `Standard Webhooks <https://www.standardwebhooks.com/>`__ signatures. Only returned
    once on create; store it securely."""

    signing_secret_last4: Optional[str] = Field(default=UNSET, alias="signingSecretLast4")
    """Last four characters of the signing secret, for display purposes."""


class WebhookEndpointDict(TypedDict):
    endpoint_id: str
    url: str
    events: list[WebhookEventNameOrStr]
    description: NotRequired[str | None]
    created_at: int
    signing_secret: NotRequired[str]
    signing_secret_last4: NotRequired[str]
