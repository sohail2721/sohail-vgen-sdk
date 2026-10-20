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
from ..models.create_file_upload_request import CreateFileUploadRequest, CreateFileUploadRequestDict
from ..models.file_info import FileInfo
from ..models.file_upload_response import FileUploadResponse
from ..models.get_files_response import GetFilesResponse
from ..models.search_files_request import SearchFilesRequest, SearchFilesRequestDict
from ..models.search_files_response import SearchFilesResponse
from ..server.server import Server


class Files:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FilesWithRawResponse(client, server, auth)

    def archive_file(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Archive a file by setting its archived timestamp. Archived files are excluded from list results. Returns the
        updated file object.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Archived file

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.archive_file(file_id, request_options=request_options))

    def create_file_upload(
        self,
        *,
        body: CreateFileUploadRequest | CreateFileUploadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileUploadResponse:
        """Create a new file and receive a pre-signed upload URL. PUT the file bytes to the returned URL, then poll
        ``GET /v1/files/{fileId}`` until the file is ready.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Upload instructions

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_file_upload(body=body, request_options=request_options))

    def disable_public_preview(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Disable public preview for a file. Removes the permanent public URL copy and revokes unauthenticated embed
        streaming access. Authenticated signed URLs remain functional. Returns the updated file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File with public preview disabled

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.disable_public_preview(file_id, request_options=request_options))

    def enable_public_preview(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Enable public preview for a file. Works for any file type. Copies the file to a permanent public URL
        (``staticPublicPreviewSource``) and, for video and audio, registers a public embed playback id
        (``publicPlaybackId``) for use with ``@videogen/player``. If streaming playback is still processing, the
        endpoint polls briefly and background processing finishes creating the embed playback id. Returns the updated
        file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File with public preview enabled

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.enable_public_preview(file_id, request_options=request_options))

    def get_file(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Retrieve metadata for a single file by its id.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File metadata

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_file(file_id, request_options=request_options))

    def get_files(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_export_files: bool | None = False,
        include_project_files: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFilesResponse:
        """List files accessible to your team. By default this returns standalone files (direct tool-call outputs and
        uploads) and omits two categories: export files (the raw output files of your exports) and project files (the
        generative files created within a project, e.g. each AI image and text-to-speech file in a script-to-video
        workflow output). Set ``includeExportFiles`` and/or ``includeProjectFiles`` to true to include them. Use
        ``selfOnly=true`` to restrict results to files created by the calling API key's user. Files are returned most
        recently updated first. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_export_files: When true, includes export files: the raw output files of your exports (the rendered
                MP4 you download from an export). When false (default), they are omitted.
            include_project_files: When true, includes project files: the generative files created within a project
                (e.g. each AI image and text-to-speech file produced inside a script-to-video workflow output). When
                false (default), they are omitted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_files(
                limit=limit,
                cursor=cursor,
                self_only=self_only,
                include_export_files=include_export_files,
                include_project_files=include_project_files,
                request_options=request_options,
            ),
        )

    def hydrate_file(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Generate fresh signed URLs for all available renditions of a file. Call this when source URLs are missing or
        expired. Returns the full file object with populated ``downloadSource``, ``thumbnailSource``, and
        ``previewSource`` (and the convenience root-level ``downloadUrl`` / ``thumbnailUrl``).

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File with hydrated sources

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.hydrate_file(file_id, request_options=request_options))

    def search_files(
        self,
        *,
        body: SearchFilesRequest | SearchFilesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchFilesResponse:
        """Semantic vector search over your files. Embeds the query text and returns the closest matching files ranked
        by cosine similarity. Only files with indexed descriptions are searchable.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search results ordered by descending similarity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_files(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> FilesWithRawResponse:
        return self._with_raw_response


class AsyncFiles:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFilesWithRawResponse(client, server, auth)

    async def archive_file(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Archive a file by setting its archived timestamp. Archived files are excluded from list results. Returns the
        updated file object.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Archived file

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.archive_file(file_id, request_options=request_options))

    async def create_file_upload(
        self,
        *,
        body: CreateFileUploadRequest | CreateFileUploadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FileUploadResponse:
        """Create a new file and receive a pre-signed upload URL. PUT the file bytes to the returned URL, then poll
        ``GET /v1/files/{fileId}`` until the file is ready.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Upload instructions

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_file_upload(body=body, request_options=request_options))

    async def disable_public_preview(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileInfo:
        """Disable public preview for a file. Removes the permanent public URL copy and revokes unauthenticated embed
        streaming access. Authenticated signed URLs remain functional. Returns the updated file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File with public preview disabled

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.disable_public_preview(file_id, request_options=request_options))

    async def enable_public_preview(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileInfo:
        """Enable public preview for a file. Works for any file type. Copies the file to a permanent public URL
        (``staticPublicPreviewSource``) and, for video and audio, registers a public embed playback id
        (``publicPlaybackId``) for use with ``@videogen/player``. If streaming playback is still processing, the
        endpoint polls briefly and background processing finishes creating the embed playback id. Returns the updated
        file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File with public preview enabled

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.enable_public_preview(file_id, request_options=request_options))

    async def get_file(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Retrieve metadata for a single file by its id.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File metadata

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_file(file_id, request_options=request_options))

    async def get_files(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_export_files: bool | None = False,
        include_project_files: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFilesResponse:
        """List files accessible to your team. By default this returns standalone files (direct tool-call outputs and
        uploads) and omits two categories: export files (the raw output files of your exports) and project files (the
        generative files created within a project, e.g. each AI image and text-to-speech file in a script-to-video
        workflow output). Set ``includeExportFiles`` and/or ``includeProjectFiles`` to true to include them. Use
        ``selfOnly=true`` to restrict results to files created by the calling API key's user. Files are returned most
        recently updated first. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_export_files: When true, includes export files: the raw output files of your exports (the rendered
                MP4 you download from an export). When false (default), they are omitted.
            include_project_files: When true, includes project files: the generative files created within a project
                (e.g. each AI image and text-to-speech file produced inside a script-to-video workflow output). When
                false (default), they are omitted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_files(
                limit=limit,
                cursor=cursor,
                self_only=self_only,
                include_export_files=include_export_files,
                include_project_files=include_project_files,
                request_options=request_options,
            ),
        )

    async def hydrate_file(self, file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileInfo:
        """Generate fresh signed URLs for all available renditions of a file. Call this when source URLs are missing or
        expired. Returns the full file object with populated ``downloadSource``, ``thumbnailSource``, and
        ``previewSource`` (and the convenience root-level ``downloadUrl`` / ``thumbnailUrl``).

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            File with hydrated sources

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.hydrate_file(file_id, request_options=request_options))

    async def search_files(
        self,
        *,
        body: SearchFilesRequest | SearchFilesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchFilesResponse:
        """Semantic vector search over your files. Embeds the query text and returns the closest matching files ranked
        by cosine similarity. Only files with indexed descriptions are searchable.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Search results ordered by descending similarity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_files(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncFilesWithRawResponse:
        return self._with_raw_response


class FilesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def archive_file(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Archive a file by setting its archived timestamp. Archived files are excluded from list results. Returns the
        updated file object.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/archive"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_file_upload(
        self,
        *,
        body: CreateFileUploadRequest | CreateFileUploadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileUploadResponse, RawError]:
        """Create a new file and receive a pre-signed upload URL. PUT the file bytes to the returned URL, then poll
        ``GET /v1/files/{fileId}`` until the file is ready.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/upload"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFileUploadRequest | CreateFileUploadRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FileUploadResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def disable_public_preview(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Disable public preview for a file. Removes the permanent public URL copy and revokes unauthenticated embed
        streaming access. Authenticated signed URLs remain functional. Returns the updated file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/disable-public-preview"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def enable_public_preview(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Enable public preview for a file. Works for any file type. Copies the file to a permanent public URL
        (``staticPublicPreviewSource``) and, for video and audio, registers a public embed playback id
        (``publicPlaybackId``) for use with ``@videogen/player``. If streaming playback is still processing, the
        endpoint polls briefly and background processing finishes creating the embed playback id. Returns the updated
        file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/enable-public-preview"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_file(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Retrieve metadata for a single file by its id.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/files/{fileId}"),
            path_params=[param[str]("fileId", file_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_files(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_export_files: bool | None = False,
        include_project_files: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFilesResponse, RawError]:
        """List files accessible to your team. By default this returns standalone files (direct tool-call outputs and
        uploads) and omits two categories: export files (the raw output files of your exports) and project files (the
        generative files created within a project, e.g. each AI image and text-to-speech file in a script-to-video
        workflow output). Set ``includeExportFiles`` and/or ``includeProjectFiles`` to true to include them. Use
        ``selfOnly=true`` to restrict results to files created by the calling API key's user. Files are returned most
        recently updated first. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_export_files: When true, includes export files: the raw output files of your exports (the rendered
                MP4 you download from an export). When false (default), they are omitted.
            include_project_files: When true, includes project files: the generative files created within a project
                (e.g. each AI image and text-to-speech file produced inside a script-to-video workflow output). When
                false (default), they are omitted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/files"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
                param[bool | None]("includeExportFiles", include_export_files),
                param[bool | None]("includeProjectFiles", include_project_files),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[GetFilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def hydrate_file(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Generate fresh signed URLs for all available renditions of a file. Call this when source URLs are missing or
        expired. Returns the full file object with populated ``downloadSource``, ``thumbnailSource``, and
        ``previewSource`` (and the convenience root-level ``downloadUrl`` / ``thumbnailUrl``).

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/hydrate"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_files(
        self,
        *,
        body: SearchFilesRequest | SearchFilesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchFilesResponse, RawError]:
        """Semantic vector search over your files. Embeds the query text and returns the closest matching files ranked
        by cosine similarity. Only files with indexed descriptions are searchable.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchFilesRequest | SearchFilesRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SearchFilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncFilesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def archive_file(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Archive a file by setting its archived timestamp. Archived files are excluded from list results. Returns the
        updated file object.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/archive"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_file_upload(
        self,
        *,
        body: CreateFileUploadRequest | CreateFileUploadRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FileUploadResponse, RawError]:
        """Create a new file and receive a pre-signed upload URL. PUT the file bytes to the returned URL, then poll
        ``GET /v1/files/{fileId}`` until the file is ready.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/upload"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFileUploadRequest | CreateFileUploadRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[FileUploadResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def disable_public_preview(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Disable public preview for a file. Removes the permanent public URL copy and revokes unauthenticated embed
        streaming access. Authenticated signed URLs remain functional. Returns the updated file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/disable-public-preview"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def enable_public_preview(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Enable public preview for a file. Works for any file type. Copies the file to a permanent public URL
        (``staticPublicPreviewSource``) and, for video and audio, registers a public embed playback id
        (``publicPlaybackId``) for use with ``@videogen/player``. If streaming playback is still processing, the
        endpoint polls briefly and background processing finishes creating the embed playback id. Returns the updated
        file.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/enable-public-preview"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_file(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Retrieve metadata for a single file by its id.

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/files/{fileId}"),
            path_params=[param[str]("fileId", file_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_files(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_export_files: bool | None = False,
        include_project_files: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFilesResponse, RawError]:
        """List files accessible to your team. By default this returns standalone files (direct tool-call outputs and
        uploads) and omits two categories: export files (the raw output files of your exports) and project files (the
        generative files created within a project, e.g. each AI image and text-to-speech file in a script-to-video
        workflow output). Set ``includeExportFiles`` and/or ``includeProjectFiles`` to true to include them. Use
        ``selfOnly=true`` to restrict results to files created by the calling API key's user. Files are returned most
        recently updated first. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_export_files: When true, includes export files: the raw output files of your exports (the rendered
                MP4 you download from an export). When false (default), they are omitted.
            include_project_files: When true, includes project files: the generative files created within a project
                (e.g. each AI image and text-to-speech file produced inside a script-to-video workflow output). When
                false (default), they are omitted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/files"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
                param[bool | None]("includeExportFiles", include_export_files),
                param[bool | None]("includeProjectFiles", include_project_files),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[GetFilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def hydrate_file(
        self, file_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileInfo, RawError]:
        """Generate fresh signed URLs for all available renditions of a file. Call this when source URLs are missing or
        expired. Returns the full file object with populated ``downloadSource``, ``thumbnailSource``, and
        ``previewSource`` (and the convenience root-level ``downloadUrl`` / ``thumbnailUrl``).

        Args:
            file_id: The file id (e.g. ``vg_file_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/{fileId}/hydrate"),
            path_params=[param[str]("fileId", file_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[FileInfo],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_files(
        self,
        *,
        body: SearchFilesRequest | SearchFilesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchFilesResponse, RawError]:
        """Semantic vector search over your files. Embeds the query text and returns the closest matching files ranked
        by cosine similarity. Only files with indexed descriptions are searchable.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/files/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchFilesRequest | SearchFilesRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SearchFilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
