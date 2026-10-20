from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    raw_error_response,
    unwrap,
)
from ..models.me_response import MeResponse
from ..server.server import Server


class Account:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountWithRawResponse(client, server, auth)

    def get_me(self, *, request_options: RequestOptionsOrDict | None = None) -> MeResponse:
        """Return the account and team behind the API key making the request. Takes no parameters. Call it as a
        connection test to confirm a key is valid and to discover the ``teamId`` and account ``email`` a key belongs to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The account and team for the authenticated API key.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_me(request_options=request_options))

    @property
    def with_raw_response(self) -> AccountWithRawResponse:
        return self._with_raw_response


class AsyncAccount:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountWithRawResponse(client, server, auth)

    async def get_me(self, *, request_options: RequestOptionsOrDict | None = None) -> MeResponse:
        """Return the account and team behind the API key making the request. Takes no parameters. Call it as a
        connection test to confirm a key is valid and to discover the ``teamId`` and account ``email`` a key belongs to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The account and team for the authenticated API key.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_me(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAccountWithRawResponse:
        return self._with_raw_response


class AccountWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_me(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MeResponse, RawError]:
        """Return the account and team behind the API key making the request. Takes no parameters. Call it as a
        connection test to confirm a key is valid and to discover the ``teamId`` and account ``email`` a key belongs to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/me"),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[MeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAccountWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_me(self, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MeResponse, RawError]:
        """Return the account and team behind the API key making the request. Takes no parameters. Call it as a
        connection test to confirm a key is valid and to discover the ``teamId`` and account ``email`` a key belongs to.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/me"),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[MeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
