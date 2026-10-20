from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.create_webhook_endpoint_request import CreateWebhookEndpointRequest, CreateWebhookEndpointRequestDict
from ..models.webhook_endpoint import WebhookEndpoint
from ..models.webhook_endpoint_list_response import WebhookEndpointListResponse
from ..server.server import Server


class Webhooks:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WebhooksWithRawResponse(client, server, auth)

    def create_webhook_endpoint(
        self,
        *,
        body: CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookEndpoint:
        """Register a new webhook endpoint to receive ``tool_execution.*``, ``workflow_run.*``, and ``file.*`` events.
        The signing secret is only returned in this response. Store it securely.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created; ``signingSecret`` is only returned in this response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_webhook_endpoint(body=body, request_options=request_options))

    def delete_webhook_endpoint(self, endpoint_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """Remove a webhook endpoint. It will stop receiving events immediately.

        Args:
            endpoint_id: The webhook endpoint id (e.g. ``ep_...``) returned by ``POST /v1/webhooks/endpoints``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Removed

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_webhook_endpoint(endpoint_id, request_options=request_options))

    def list_webhook_endpoints(
        self, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> WebhookEndpointListResponse:
        """List configured webhook endpoints for your account. Cursor-paginated; see the `Pagination </pagination>`__
        guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Configured endpoints

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_webhook_endpoints(limit=limit, cursor=cursor, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> WebhooksWithRawResponse:
        return self._with_raw_response


class AsyncWebhooks:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWebhooksWithRawResponse(client, server, auth)

    async def create_webhook_endpoint(
        self,
        *,
        body: CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WebhookEndpoint:
        """Register a new webhook endpoint to receive ``tool_execution.*``, ``workflow_run.*``, and ``file.*`` events.
        The signing secret is only returned in this response. Store it securely.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created; ``signingSecret`` is only returned in this response.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_webhook_endpoint(body=body, request_options=request_options))

    async def delete_webhook_endpoint(
        self, endpoint_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Remove a webhook endpoint. It will stop receiving events immediately.

        Args:
            endpoint_id: The webhook endpoint id (e.g. ``ep_...``) returned by ``POST /v1/webhooks/endpoints``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Removed

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_webhook_endpoint(endpoint_id, request_options=request_options)
        )

    async def list_webhook_endpoints(
        self, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> WebhookEndpointListResponse:
        """List configured webhook endpoints for your account. Cursor-paginated; see the `Pagination </pagination>`__
        guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Configured endpoints

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_webhook_endpoints(
                limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWebhooksWithRawResponse:
        return self._with_raw_response


class WebhooksWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_webhook_endpoint(
        self,
        *,
        body: CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookEndpoint, RawError]:
        """Register a new webhook endpoint to receive ``tool_execution.*``, ``workflow_run.*``, and ``file.*`` events.
        The signing secret is only returned in this response. Store it securely.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/webhooks/endpoints"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WebhookEndpoint],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_webhook_endpoint(
        self, endpoint_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Remove a webhook endpoint. It will stop receiving events immediately.

        Args:
            endpoint_id: The webhook endpoint id (e.g. ``ep_...``) returned by ``POST /v1/webhooks/endpoints``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/webhooks/endpoints/{endpointId}"),
            path_params=[param[str]("endpointId", endpoint_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_webhook_endpoints(
        self, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WebhookEndpointListResponse, RawError]:
        """List configured webhook endpoints for your account. Cursor-paginated; see the `Pagination </pagination>`__
        guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/webhooks/endpoints"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WebhookEndpointListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWebhooksWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_webhook_endpoint(
        self,
        *,
        body: CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WebhookEndpoint, RawError]:
        """Register a new webhook endpoint to receive ``tool_execution.*``, ``workflow_run.*``, and ``file.*`` events.
        The signing secret is only returned in this response. Store it securely.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/webhooks/endpoints"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WebhookEndpoint],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_webhook_endpoint(
        self, endpoint_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, RawError]:
        """Remove a webhook endpoint. It will stop receiving events immediately.

        Args:
            endpoint_id: The webhook endpoint id (e.g. ``ep_...``) returned by ``POST /v1/webhooks/endpoints``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v1/webhooks/endpoints/{endpointId}"),
            path_params=[param[str]("endpointId", endpoint_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Any],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_webhook_endpoints(
        self, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WebhookEndpointListResponse, RawError]:
        """List configured webhook endpoints for your account. Cursor-paginated; see the `Pagination </pagination>`__
        guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/webhooks/endpoints"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WebhookEndpointListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
