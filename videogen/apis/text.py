from __future__ import annotations

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
from ..models.generate_text_request import GenerateTextRequest, GenerateTextRequestDict
from ..models.generate_text_response import GenerateTextResponse
from ..server.server import Server


class Text:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TextWithRawResponse(client, server, auth)

    def generate_text(
        self,
        *,
        body: GenerateTextRequest | GenerateTextRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateTextResponse:
        """Generate text from a prompt using a general-purpose language model. Choose a quality tier with ``quality``
        (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Synchronous: the response includes the generated text. Useful for
        drafting scripts, titles, descriptions, and other short copy before generating a video.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Generated text.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_text(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> TextWithRawResponse:
        return self._with_raw_response


class AsyncText:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTextWithRawResponse(client, server, auth)

    async def generate_text(
        self,
        *,
        body: GenerateTextRequest | GenerateTextRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateTextResponse:
        """Generate text from a prompt using a general-purpose language model. Choose a quality tier with ``quality``
        (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Synchronous: the response includes the generated text. Useful for
        drafting scripts, titles, descriptions, and other short copy before generating a video.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Generated text.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_text(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncTextWithRawResponse:
        return self._with_raw_response


class TextWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def generate_text(
        self,
        *,
        body: GenerateTextRequest | GenerateTextRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateTextResponse, RawError]:
        """Generate text from a prompt using a general-purpose language model. Choose a quality tier with ``quality``
        (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Synchronous: the response includes the generated text. Useful for
        drafting scripts, titles, descriptions, and other short copy before generating a video.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/text/generate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateTextRequest | GenerateTextRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[GenerateTextResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTextWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def generate_text(
        self,
        *,
        body: GenerateTextRequest | GenerateTextRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateTextResponse, RawError]:
        """Generate text from a prompt using a general-purpose language model. Choose a quality tier with ``quality``
        (``LOW``, ``STANDARD``, ``HIGH``, or ``MAX``). Synchronous: the response includes the generated text. Useful for
        drafting scripts, titles, descriptions, and other short copy before generating a video.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/text/generate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateTextRequest | GenerateTextRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[GenerateTextResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
