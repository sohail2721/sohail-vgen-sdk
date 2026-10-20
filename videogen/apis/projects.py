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
from ..models.create_timeline_interchange_request import (
    CreateTimelineInterchangeRequest,
    CreateTimelineInterchangeRequestDict,
)
from ..models.create_timeline_interchange_response import CreateTimelineInterchangeResponse
from ..models.export_project_request import ExportProjectRequest, ExportProjectRequestDict
from ..models.export_project_response import ExportProjectResponse
from ..models.list_project_exports_response import ListProjectExportsResponse
from ..models.list_projects_response import ListProjectsResponse
from ..models.list_remix_actions_response import ListRemixActionsResponse
from ..models.project_export import ProjectExport
from ..models.project_response import ProjectResponse
from ..models.remix_project_request import RemixProjectRequest, RemixProjectRequestDict
from ..models.remix_project_response import RemixProjectResponse
from ..models.timeline_interchange import TimelineInterchange
from ..server.server import Server


class Projects:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProjectsWithRawResponse(client, server, auth)

    def create_timeline_interchange(
        self,
        project_id: str,
        *,
        body: CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTimelineInterchangeResponse:
        """Starts a timeline interchange job that converts a project into an editor interchange document (Final Cut Pro
        FCPXML, Adobe Premiere Pro XML, OpenTimelineIO, or an SRT caption sidecar). Returns immediately with an
        interchange job id; the file becomes available when the job completes. Unlike ``POST
        /v1/projects/{projectId}/export`` (which renders a flattened MP4), this preserves the project as an editable
        timeline of separate clips, tracks, and captions so you can keep editing it in a desktop video editor. Choose
        ``mediaDelivery`` to control how the document references media: ``REMOTE_URLS`` produces a single document that
        links to signed media URLs, while ``BUNDLE`` produces a zip containing the document plus every referenced media
        file for durable offline relinking.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Timeline interchange accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.create_timeline_interchange(project_id, body=body, request_options=request_options)
        )

    def export_project(
        self,
        project_id: str,
        *,
        body: ExportProjectRequest | ExportProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ExportProjectResponse:
        """Starts an export of a project to MP4. Returns immediately with an export id; the file becomes available when
        the export task completes. Exporting requires a paid plan in the app, but the API lets you export for free with
        a VideoGen watermark and a short 'Made with VideoGen' end screen appended to the video. A Pro plan lets you
        remove both by setting ``watermarkMode`` and ``endScreenMode`` to ``NONE``.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Export accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.export_project(project_id, body=body, request_options=request_options))

    def get_project(self, project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ProjectResponse:
        """Returns a simplified view of a project including its title, aspect ratio, status, and URL.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Project metadata.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_project(project_id, request_options=request_options))

    def get_project_export(
        self, project_id: str, export_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProjectExport:
        """Returns the current status of a project export started via ``POST /v1/projects/{projectId}/export``, and —
        once ``status`` is ``succeeded`` — the signed download/thumbnail URLs and the hydrated export ``file``. Poll
        this endpoint until ``status`` is ``succeeded``, ``failed``, or ``cancelled``. The signed URLs are private and
        valid for 7 days; this endpoint automatically re-signs them when they are within an hour of expiring, so a
        caller always receives a URL valid long enough to use. Every endpoint that returns hydrated files
        auto-rehydrates this way — only the file endpoints (``GET /v1/files/{fileId}`` and ``POST
        /v1/files/{fileId}/hydrate``) are the explicit, on-demand hydration paths. Use ``exportFileId`` with ``POST
        /v1/files/{fileId}/hydrate`` if you need to re-sign the export file directly later.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            export_id: The export id (e.g. ``vg_expo_...``) returned by ``POST /v1/projects/{projectId}/export``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Export status.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_project_export(project_id, export_id, request_options=request_options)
        )

    def get_timeline_interchange(
        self, interchange_job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TimelineInterchange:
        """Returns the current status of a timeline interchange job started via ``POST
        /v1/projects/{projectId}/timeline-interchange``, and, once ``status`` is ``succeeded``, the signed download URL
        and the hydrated interchange ``file``. Poll this endpoint until ``status`` is ``succeeded``, ``failed``, or
        ``cancelled``. The signed URL is private and valid for 7 days; this endpoint automatically re-signs it when it
        is within an hour of expiring. Use ``interchangeFileId`` with ``POST /v1/files/{fileId}/hydrate`` if you need to
        re-sign the file directly later.

        Args:
            interchange_job_id: The timeline interchange job id (e.g. ``vg_inte_...``) returned by ``POST
                /v1/projects/{projectId}/timeline-interchange``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Timeline interchange status.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_timeline_interchange(interchange_job_id, request_options=request_options)
        )

    def list_project_exports(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectExportsResponse:
        """Returns a project's exports, newest first, as fully hydrated ``ProjectExport`` objects (status, signed
        download/thumbnail URLs, and the embedded ``file``). Signed URLs are re-signed when within an hour of expiring,
        so they are always valid long enough to use. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Project exports.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_project_exports(
                project_id, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    def list_project_remix_actions(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRemixActionsResponse:
        """Returns remix actions applied to a project (via ``POST /v1/projects/{projectId}/remix`` or as a post-workflow
        step), most recent first, with each action's status and progress. Cursor-paginated; see the `Pagination
        </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Remix actions for the project.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_project_remix_actions(
                project_id, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    def list_projects(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_ui_projects: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectsResponse:
        """Returns projects, most recently updated first. By default only API-created projects are included; pass
        ``includeUiProjects=true`` to also include dashboard-created projects. Use ``selfOnly=true`` to restrict results
        to the calling API key's user; otherwise all matching projects for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_ui_projects: When true, includes dashboard-created projects in addition to API-created projects.
                When false (default), returns only API-created projects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Paginated list of projects.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_projects(
                limit=limit,
                cursor=cursor,
                self_only=self_only,
                include_ui_projects=include_ui_projects,
                request_options=request_options,
            ),
        )

    def remix_project(
        self,
        project_id: str,
        *,
        body: RemixProjectRequest | RemixProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemixProjectResponse:
        """Applies an ordered list of edits (background music, logo overlay, caption visibility/style) to a project.
        Each action runs asynchronously as its own remix action; the response returns one remix action id per action in
        order. Set ``saveAsNewProject`` to apply the edits to a copy and leave the original untouched. Poll ``GET
        /v1/projects/{projectId}/remix-actions`` for status.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Remix actions accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.remix_project(project_id, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> ProjectsWithRawResponse:
        return self._with_raw_response


class AsyncProjects:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProjectsWithRawResponse(client, server, auth)

    async def create_timeline_interchange(
        self,
        project_id: str,
        *,
        body: CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTimelineInterchangeResponse:
        """Starts a timeline interchange job that converts a project into an editor interchange document (Final Cut Pro
        FCPXML, Adobe Premiere Pro XML, OpenTimelineIO, or an SRT caption sidecar). Returns immediately with an
        interchange job id; the file becomes available when the job completes. Unlike ``POST
        /v1/projects/{projectId}/export`` (which renders a flattened MP4), this preserves the project as an editable
        timeline of separate clips, tracks, and captions so you can keep editing it in a desktop video editor. Choose
        ``mediaDelivery`` to control how the document references media: ``REMOTE_URLS`` produces a single document that
        links to signed media URLs, while ``BUNDLE`` produces a zip containing the document plus every referenced media
        file for durable offline relinking.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Timeline interchange accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.create_timeline_interchange(
                project_id, body=body, request_options=request_options
            ),
        )

    async def export_project(
        self,
        project_id: str,
        *,
        body: ExportProjectRequest | ExportProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ExportProjectResponse:
        """Starts an export of a project to MP4. Returns immediately with an export id; the file becomes available when
        the export task completes. Exporting requires a paid plan in the app, but the API lets you export for free with
        a VideoGen watermark and a short 'Made with VideoGen' end screen appended to the video. A Pro plan lets you
        remove both by setting ``watermarkMode`` and ``endScreenMode`` to ``NONE``.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Export accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.export_project(project_id, body=body, request_options=request_options)
        )

    async def get_project(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProjectResponse:
        """Returns a simplified view of a project including its title, aspect ratio, status, and URL.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Project metadata.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_project(project_id, request_options=request_options))

    async def get_project_export(
        self, project_id: str, export_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ProjectExport:
        """Returns the current status of a project export started via ``POST /v1/projects/{projectId}/export``, and —
        once ``status`` is ``succeeded`` — the signed download/thumbnail URLs and the hydrated export ``file``. Poll
        this endpoint until ``status`` is ``succeeded``, ``failed``, or ``cancelled``. The signed URLs are private and
        valid for 7 days; this endpoint automatically re-signs them when they are within an hour of expiring, so a
        caller always receives a URL valid long enough to use. Every endpoint that returns hydrated files
        auto-rehydrates this way — only the file endpoints (``GET /v1/files/{fileId}`` and ``POST
        /v1/files/{fileId}/hydrate``) are the explicit, on-demand hydration paths. Use ``exportFileId`` with ``POST
        /v1/files/{fileId}/hydrate`` if you need to re-sign the export file directly later.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            export_id: The export id (e.g. ``vg_expo_...``) returned by ``POST /v1/projects/{projectId}/export``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Export status.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_project_export(project_id, export_id, request_options=request_options)
        )

    async def get_timeline_interchange(
        self, interchange_job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TimelineInterchange:
        """Returns the current status of a timeline interchange job started via ``POST
        /v1/projects/{projectId}/timeline-interchange``, and, once ``status`` is ``succeeded``, the signed download URL
        and the hydrated interchange ``file``. Poll this endpoint until ``status`` is ``succeeded``, ``failed``, or
        ``cancelled``. The signed URL is private and valid for 7 days; this endpoint automatically re-signs it when it
        is within an hour of expiring. Use ``interchangeFileId`` with ``POST /v1/files/{fileId}/hydrate`` if you need to
        re-sign the file directly later.

        Args:
            interchange_job_id: The timeline interchange job id (e.g. ``vg_inte_...``) returned by ``POST
                /v1/projects/{projectId}/timeline-interchange``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Timeline interchange status.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_timeline_interchange(interchange_job_id, request_options=request_options)
        )

    async def list_project_exports(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectExportsResponse:
        """Returns a project's exports, newest first, as fully hydrated ``ProjectExport`` objects (status, signed
        download/thumbnail URLs, and the embedded ``file``). Signed URLs are re-signed when within an hour of expiring,
        so they are always valid long enough to use. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Project exports.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_project_exports(
                project_id, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    async def list_project_remix_actions(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListRemixActionsResponse:
        """Returns remix actions applied to a project (via ``POST /v1/projects/{projectId}/remix`` or as a post-workflow
        step), most recent first, with each action's status and progress. Cursor-paginated; see the `Pagination
        </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Remix actions for the project.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_project_remix_actions(
                project_id, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    async def list_projects(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_ui_projects: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListProjectsResponse:
        """Returns projects, most recently updated first. By default only API-created projects are included; pass
        ``includeUiProjects=true`` to also include dashboard-created projects. Use ``selfOnly=true`` to restrict results
        to the calling API key's user; otherwise all matching projects for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_ui_projects: When true, includes dashboard-created projects in addition to API-created projects.
                When false (default), returns only API-created projects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Paginated list of projects.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_projects(
                limit=limit,
                cursor=cursor,
                self_only=self_only,
                include_ui_projects=include_ui_projects,
                request_options=request_options,
            ),
        )

    async def remix_project(
        self,
        project_id: str,
        *,
        body: RemixProjectRequest | RemixProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RemixProjectResponse:
        """Applies an ordered list of edits (background music, logo overlay, caption visibility/style) to a project.
        Each action runs asynchronously as its own remix action; the response returns one remix action id per action in
        order. Set ``saveAsNewProject`` to apply the edits to a copy and leave the original untouched. Poll ``GET
        /v1/projects/{projectId}/remix-actions`` for status.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Remix actions accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.remix_project(project_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncProjectsWithRawResponse:
        return self._with_raw_response


class ProjectsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_timeline_interchange(
        self,
        project_id: str,
        *,
        body: CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTimelineInterchangeResponse, RawError]:
        """Starts a timeline interchange job that converts a project into an editor interchange document (Final Cut Pro
        FCPXML, Adobe Premiere Pro XML, OpenTimelineIO, or an SRT caption sidecar). Returns immediately with an
        interchange job id; the file becomes available when the job completes. Unlike ``POST
        /v1/projects/{projectId}/export`` (which renders a flattened MP4), this preserves the project as an editable
        timeline of separate clips, tracks, and captions so you can keep editing it in a desktop video editor. Choose
        ``mediaDelivery`` to control how the document references media: ``REMOTE_URLS`` produces a single document that
        links to signed media URLs, while ``BUNDLE`` produces a zip containing the document plus every referenced media
        file for durable offline relinking.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{projectId}/timeline-interchange"),
            path_params=[param[str]("projectId", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[CreateTimelineInterchangeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def export_project(
        self,
        project_id: str,
        *,
        body: ExportProjectRequest | ExportProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ExportProjectResponse, RawError]:
        """Starts an export of a project to MP4. Returns immediately with an export id; the file becomes available when
        the export task completes. Exporting requires a paid plan in the app, but the API lets you export for free with
        a VideoGen watermark and a short 'Made with VideoGen' end screen appended to the video. A Pro plan lets you
        remove both by setting ``watermarkMode`` and ``endScreenMode`` to ``NONE``.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{projectId}/export"),
            path_params=[param[str]("projectId", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ExportProjectRequest | ExportProjectRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ExportProjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_project(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProjectResponse, RawError]:
        """Returns a simplified view of a project including its title, aspect ratio, status, and URL.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{projectId}"),
            path_params=[param[str]("projectId", project_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ProjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_project_export(
        self, project_id: str, export_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProjectExport, RawError]:
        """Returns the current status of a project export started via ``POST /v1/projects/{projectId}/export``, and —
        once ``status`` is ``succeeded`` — the signed download/thumbnail URLs and the hydrated export ``file``. Poll
        this endpoint until ``status`` is ``succeeded``, ``failed``, or ``cancelled``. The signed URLs are private and
        valid for 7 days; this endpoint automatically re-signs them when they are within an hour of expiring, so a
        caller always receives a URL valid long enough to use. Every endpoint that returns hydrated files
        auto-rehydrates this way — only the file endpoints (``GET /v1/files/{fileId}`` and ``POST
        /v1/files/{fileId}/hydrate``) are the explicit, on-demand hydration paths. Use ``exportFileId`` with ``POST
        /v1/files/{fileId}/hydrate`` if you need to re-sign the export file directly later.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            export_id: The export id (e.g. ``vg_expo_...``) returned by ``POST /v1/projects/{projectId}/export``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{projectId}/exports/{exportId}"),
            path_params=[param[str]("projectId", project_id), param[str]("exportId", export_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ProjectExport],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_timeline_interchange(
        self, interchange_job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TimelineInterchange, RawError]:
        """Returns the current status of a timeline interchange job started via ``POST
        /v1/projects/{projectId}/timeline-interchange``, and, once ``status`` is ``succeeded``, the signed download URL
        and the hydrated interchange ``file``. Poll this endpoint until ``status`` is ``succeeded``, ``failed``, or
        ``cancelled``. The signed URL is private and valid for 7 days; this endpoint automatically re-signs it when it
        is within an hour of expiring. Use ``interchangeFileId`` with ``POST /v1/files/{fileId}/hydrate`` if you need to
        re-sign the file directly later.

        Args:
            interchange_job_id: The timeline interchange job id (e.g. ``vg_inte_...``) returned by ``POST
                /v1/projects/{projectId}/timeline-interchange``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/timeline-interchange/{interchangeJobId}"),
            path_params=[param[str]("interchangeJobId", interchange_job_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[TimelineInterchange],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_project_exports(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectExportsResponse, RawError]:
        """Returns a project's exports, newest first, as fully hydrated ``ProjectExport`` objects (status, signed
        download/thumbnail URLs, and the embedded ``file``). Signed URLs are re-signed when within an hour of expiring,
        so they are always valid long enough to use. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
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
            url_template=self._server.default("/v1/projects/{projectId}/exports"),
            path_params=[param[str]("projectId", project_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ListProjectExportsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_project_remix_actions(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRemixActionsResponse, RawError]:
        """Returns remix actions applied to a project (via ``POST /v1/projects/{projectId}/remix`` or as a post-workflow
        step), most recent first, with each action's status and progress. Cursor-paginated; see the `Pagination
        </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
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
            url_template=self._server.default("/v1/projects/{projectId}/remix-actions"),
            path_params=[param[str]("projectId", project_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ListRemixActionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_projects(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_ui_projects: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectsResponse, RawError]:
        """Returns projects, most recently updated first. By default only API-created projects are included; pass
        ``includeUiProjects=true`` to also include dashboard-created projects. Use ``selfOnly=true`` to restrict results
        to the calling API key's user; otherwise all matching projects for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_ui_projects: When true, includes dashboard-created projects in addition to API-created projects.
                When false (default), returns only API-created projects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
                param[bool | None]("includeUiProjects", include_ui_projects),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ListProjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remix_project(
        self,
        project_id: str,
        *,
        body: RemixProjectRequest | RemixProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemixProjectResponse, RawError]:
        """Applies an ordered list of edits (background music, logo overlay, caption visibility/style) to a project.
        Each action runs asynchronously as its own remix action; the response returns one remix action id per action in
        order. Set ``saveAsNewProject`` to apply the edits to a copy and leave the original untouched. Poll ``GET
        /v1/projects/{projectId}/remix-actions`` for status.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{projectId}/remix"),
            path_params=[param[str]("projectId", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemixProjectRequest | RemixProjectRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[RemixProjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncProjectsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_timeline_interchange(
        self,
        project_id: str,
        *,
        body: CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTimelineInterchangeResponse, RawError]:
        """Starts a timeline interchange job that converts a project into an editor interchange document (Final Cut Pro
        FCPXML, Adobe Premiere Pro XML, OpenTimelineIO, or an SRT caption sidecar). Returns immediately with an
        interchange job id; the file becomes available when the job completes. Unlike ``POST
        /v1/projects/{projectId}/export`` (which renders a flattened MP4), this preserves the project as an editable
        timeline of separate clips, tracks, and captions so you can keep editing it in a desktop video editor. Choose
        ``mediaDelivery`` to control how the document references media: ``REMOTE_URLS`` produces a single document that
        links to signed media URLs, while ``BUNDLE`` produces a zip containing the document plus every referenced media
        file for durable offline relinking.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{projectId}/timeline-interchange"),
            path_params=[param[str]("projectId", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[CreateTimelineInterchangeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def export_project(
        self,
        project_id: str,
        *,
        body: ExportProjectRequest | ExportProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ExportProjectResponse, RawError]:
        """Starts an export of a project to MP4. Returns immediately with an export id; the file becomes available when
        the export task completes. Exporting requires a paid plan in the app, but the API lets you export for free with
        a VideoGen watermark and a short 'Made with VideoGen' end screen appended to the video. A Pro plan lets you
        remove both by setting ``watermarkMode`` and ``endScreenMode`` to ``NONE``.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{projectId}/export"),
            path_params=[param[str]("projectId", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ExportProjectRequest | ExportProjectRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ExportProjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_project(
        self, project_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProjectResponse, RawError]:
        """Returns a simplified view of a project including its title, aspect ratio, status, and URL.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{projectId}"),
            path_params=[param[str]("projectId", project_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ProjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_project_export(
        self, project_id: str, export_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ProjectExport, RawError]:
        """Returns the current status of a project export started via ``POST /v1/projects/{projectId}/export``, and —
        once ``status`` is ``succeeded`` — the signed download/thumbnail URLs and the hydrated export ``file``. Poll
        this endpoint until ``status`` is ``succeeded``, ``failed``, or ``cancelled``. The signed URLs are private and
        valid for 7 days; this endpoint automatically re-signs them when they are within an hour of expiring, so a
        caller always receives a URL valid long enough to use. Every endpoint that returns hydrated files
        auto-rehydrates this way — only the file endpoints (``GET /v1/files/{fileId}`` and ``POST
        /v1/files/{fileId}/hydrate``) are the explicit, on-demand hydration paths. Use ``exportFileId`` with ``POST
        /v1/files/{fileId}/hydrate`` if you need to re-sign the export file directly later.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            export_id: The export id (e.g. ``vg_expo_...``) returned by ``POST /v1/projects/{projectId}/export``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects/{projectId}/exports/{exportId}"),
            path_params=[param[str]("projectId", project_id), param[str]("exportId", export_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ProjectExport],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_timeline_interchange(
        self, interchange_job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TimelineInterchange, RawError]:
        """Returns the current status of a timeline interchange job started via ``POST
        /v1/projects/{projectId}/timeline-interchange``, and, once ``status`` is ``succeeded``, the signed download URL
        and the hydrated interchange ``file``. Poll this endpoint until ``status`` is ``succeeded``, ``failed``, or
        ``cancelled``. The signed URL is private and valid for 7 days; this endpoint automatically re-signs it when it
        is within an hour of expiring. Use ``interchangeFileId`` with ``POST /v1/files/{fileId}/hydrate`` if you need to
        re-sign the file directly later.

        Args:
            interchange_job_id: The timeline interchange job id (e.g. ``vg_inte_...``) returned by ``POST
                /v1/projects/{projectId}/timeline-interchange``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/timeline-interchange/{interchangeJobId}"),
            path_params=[param[str]("interchangeJobId", interchange_job_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[TimelineInterchange],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_project_exports(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectExportsResponse, RawError]:
        """Returns a project's exports, newest first, as fully hydrated ``ProjectExport`` objects (status, signed
        download/thumbnail URLs, and the embedded ``file``). Signed URLs are re-signed when within an hour of expiring,
        so they are always valid long enough to use. Cursor-paginated; see the `Pagination </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
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
            url_template=self._server.default("/v1/projects/{projectId}/exports"),
            path_params=[param[str]("projectId", project_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ListProjectExportsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_project_remix_actions(
        self,
        project_id: str,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListRemixActionsResponse, RawError]:
        """Returns remix actions applied to a project (via ``POST /v1/projects/{projectId}/remix`` or as a post-workflow
        step), most recent first, with each action's status and progress. Cursor-paginated; see the `Pagination
        </pagination>`__ guide.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
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
            url_template=self._server.default("/v1/projects/{projectId}/remix-actions"),
            path_params=[param[str]("projectId", project_id)],
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ListRemixActionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_projects(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        include_ui_projects: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListProjectsResponse, RawError]:
        """Returns projects, most recently updated first. By default only API-created projects are included; pass
        ``includeUiProjects=true`` to also include dashboard-created projects. Use ``selfOnly=true`` to restrict results
        to the calling API key's user; otherwise all matching projects for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            include_ui_projects: When true, includes dashboard-created projects in addition to API-created projects.
                When false (default), returns only API-created projects.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/projects"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
                param[bool | None]("includeUiProjects", include_ui_projects),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ListProjectsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remix_project(
        self,
        project_id: str,
        *,
        body: RemixProjectRequest | RemixProjectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RemixProjectResponse, RawError]:
        """Applies an ordered list of edits (background music, logo overlay, caption visibility/style) to a project.
        Each action runs asynchronously as its own remix action; the response returns one remix action id per action in
        order. Set ``saveAsNewProject`` to apply the edits to a copy and leave the original untouched. Poll ``GET
        /v1/projects/{projectId}/remix-actions`` for status.

        Args:
            project_id: The project id (e.g. ``vg_proj_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/projects/{projectId}/remix"),
            path_params=[param[str]("projectId", project_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemixProjectRequest | RemixProjectRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[RemixProjectResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
