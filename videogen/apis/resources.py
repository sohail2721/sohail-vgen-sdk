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
    param,
    raw_error_response,
    unwrap,
)
from ..models.language_list_response import LanguageListResponse
from ..models.tts_voice_list_response import TtsVoiceListResponse
from ..server.server import Server


class Resources:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ResourcesWithRawResponse(client, server, auth)

    def list_languages(
        self, *, query: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> LanguageListResponse:
        """List the languages a project can be translated into. Pass a ``languageCode`` from the response to the
        ``TRANSLATE_PROJECT`` remix action. Returns the full catalogue in a single response (not paginated). Pass
        ``query`` to filter by language code or English name.

        Args:
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            List of supported languages. Pass a ``languageCode`` to a ``TRANSLATE_PROJECT`` remix action.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.list_languages(query=query, request_options=request_options))

    def list_tts_voices(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        include_deprecated_voices: bool | None = False,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TtsVoiceListResponse:
        """List available text-to-speech voices. Pass a ``voiceId`` or ``displayName`` from the response to the
        text-to-speech endpoint. Cursor-paginated; see the `Pagination </pagination>`__ guide. Pass ``query`` to filter
        by voice id, display name, language, accent, or description.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            include_deprecated_voices: When true, includes voices that are deprecated but still callable. Defaults to
                false.
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            List of TTS voices. Pass a ``voiceId`` or ``displayName`` to ``POST /v1/tools/text-to-speech``.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_tts_voices(
                limit=limit,
                cursor=cursor,
                include_deprecated_voices=include_deprecated_voices,
                query=query,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ResourcesWithRawResponse:
        return self._with_raw_response


class AsyncResources:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncResourcesWithRawResponse(client, server, auth)

    async def list_languages(
        self, *, query: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> LanguageListResponse:
        """List the languages a project can be translated into. Pass a ``languageCode`` from the response to the
        ``TRANSLATE_PROJECT`` remix action. Returns the full catalogue in a single response (not paginated). Pass
        ``query`` to filter by language code or English name.

        Args:
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            List of supported languages. Pass a ``languageCode`` to a ``TRANSLATE_PROJECT`` remix action.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.list_languages(query=query, request_options=request_options))

    async def list_tts_voices(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        include_deprecated_voices: bool | None = False,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TtsVoiceListResponse:
        """List available text-to-speech voices. Pass a ``voiceId`` or ``displayName`` from the response to the
        text-to-speech endpoint. Cursor-paginated; see the `Pagination </pagination>`__ guide. Pass ``query`` to filter
        by voice id, display name, language, accent, or description.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            include_deprecated_voices: When true, includes voices that are deprecated but still callable. Defaults to
                false.
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            List of TTS voices. Pass a ``voiceId`` or ``displayName`` to ``POST /v1/tools/text-to-speech``.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_tts_voices(
                limit=limit,
                cursor=cursor,
                include_deprecated_voices=include_deprecated_voices,
                query=query,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncResourcesWithRawResponse:
        return self._with_raw_response


class ResourcesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_languages(
        self, *, query: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LanguageListResponse, RawError]:
        """List the languages a project can be translated into. Pass a ``languageCode`` from the response to the
        ``TRANSLATE_PROJECT`` remix action. Returns the full catalogue in a single response (not paginated). Pass
        ``query`` to filter by language code or English name.

        Args:
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/resources/languages"),
            query_params=[param[str | None]("query", query)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[LanguageListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_tts_voices(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        include_deprecated_voices: bool | None = False,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TtsVoiceListResponse, RawError]:
        """List available text-to-speech voices. Pass a ``voiceId`` or ``displayName`` from the response to the
        text-to-speech endpoint. Cursor-paginated; see the `Pagination </pagination>`__ guide. Pass ``query`` to filter
        by voice id, display name, language, accent, or description.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            include_deprecated_voices: When true, includes voices that are deprecated but still callable. Defaults to
                false.
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/resources/tts-voices"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("includeDeprecatedVoices", include_deprecated_voices),
                param[str | None]("query", query),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TtsVoiceListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncResourcesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_languages(
        self, *, query: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[LanguageListResponse, RawError]:
        """List the languages a project can be translated into. Pass a ``languageCode`` from the response to the
        ``TRANSLATE_PROJECT`` remix action. Returns the full catalogue in a single response (not paginated). Pass
        ``query`` to filter by language code or English name.

        Args:
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/resources/languages"),
            query_params=[param[str | None]("query", query)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[LanguageListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_tts_voices(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        include_deprecated_voices: bool | None = False,
        query: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TtsVoiceListResponse, RawError]:
        """List available text-to-speech voices. Pass a ``voiceId`` or ``displayName`` from the response to the
        text-to-speech endpoint. Cursor-paginated; see the `Pagination </pagination>`__ guide. Pass ``query`` to filter
        by voice id, display name, language, accent, or description.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            include_deprecated_voices: When true, includes voices that are deprecated but still callable. Defaults to
                false.
            query: Optional case-insensitive substring filter across each item's searchable text fields. Omit to return
                the unfiltered catalogue.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/resources/tts-voices"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("includeDeprecatedVoices", include_deprecated_voices),
                param[str | None]("query", query),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[TtsVoiceListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
