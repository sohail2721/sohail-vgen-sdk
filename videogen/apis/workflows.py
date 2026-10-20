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
from ..models.prompt_to_video_clip_request import PromptToVideoClipRequest, PromptToVideoClipRequestDict
from ..models.script_to_video_request import ScriptToVideoRequest, ScriptToVideoRequestDict
from ..models.slideshow_to_video_request import SlideshowToVideoRequest, SlideshowToVideoRequestDict
from ..models.start_workflow_run_response import StartWorkflowRunResponse
from ..models.voiceover_to_video_request import VoiceoverToVideoRequest, VoiceoverToVideoRequestDict
from ..models.workflow_run import WorkflowRun
from ..models.workflow_run_list_response import WorkflowRunListResponse
from ..server.server import Server


class Workflows:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WorkflowsWithRawResponse(client, server, auth)

    def cancel_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StartWorkflowRunResponse:
        """Send a ``POST`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation request accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.cancel_workflow_run(workflow_run_id, request_options=request_options))

    def get_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WorkflowRun:
        """Send a ``GET`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Current workflow run state.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_workflow_run(workflow_run_id, request_options=request_options))

    def list_workflow_runs(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WorkflowRunListResponse:
        """List workflow runs started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all runs for the team are returned. Cursor-paginated; see the
        `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Paginated list of workflow runs.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_workflow_runs(
                limit=limit, cursor=cursor, self_only=self_only, request_options=request_options
            ),
        )

    def prompt_to_video_clip(
        self,
        *,
        body: PromptToVideoClipRequest | PromptToVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project from a text prompt and generates one short AI video clip (up to 30 seconds). VideoGen first
        generates an opening frame from the prompt (optionally guided by reference images), then animates that frame
        into a video. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion. For a
        standalone clip without an editable project, use ``POST /v1/tools/generate-video-clip`` instead. For longer
        narrated multi-scene videos, use ``POST /v1/workflows/script-to-video``. The generated clip is clamped to the
        selected quality's supported range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.prompt_to_video_clip(body=body, request_options=request_options))

    def script_to_video(
        self,
        *,
        body: ScriptToVideoRequest | ScriptToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project and generates a narrated video from a prompt or script. Returns immediately with a workflow
        run id; poll or subscribe to webhooks for completion.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.script_to_video(body=body, request_options=request_options))

    def slideshow_to_video(
        self,
        *,
        body: SlideshowToVideoRequest | SlideshowToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project from an uploaded PDF or PowerPoint file and generates an AI-narrated video walking through
        each slide. Upload the file via ``POST /v1/files/upload`` first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.slideshow_to_video(body=body, request_options=request_options))

    def voiceover_to_video(
        self,
        *,
        body: VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project from an uploaded voiceover file and generates a video with matching b-roll. Upload the
        voiceover via the files API first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.voiceover_to_video(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> WorkflowsWithRawResponse:
        return self._with_raw_response


class AsyncWorkflows:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWorkflowsWithRawResponse(client, server, auth)

    async def cancel_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StartWorkflowRunResponse:
        """Send a ``POST`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation request accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_workflow_run(workflow_run_id, request_options=request_options)
        )

    async def get_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> WorkflowRun:
        """Send a ``GET`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Current workflow run state.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_workflow_run(workflow_run_id, request_options=request_options))

    async def list_workflow_runs(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WorkflowRunListResponse:
        """List workflow runs started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all runs for the team are returned. Cursor-paginated; see the
        `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Paginated list of workflow runs.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_workflow_runs(
                limit=limit, cursor=cursor, self_only=self_only, request_options=request_options
            ),
        )

    async def prompt_to_video_clip(
        self,
        *,
        body: PromptToVideoClipRequest | PromptToVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project from a text prompt and generates one short AI video clip (up to 30 seconds). VideoGen first
        generates an opening frame from the prompt (optionally guided by reference images), then animates that frame
        into a video. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion. For a
        standalone clip without an editable project, use ``POST /v1/tools/generate-video-clip`` instead. For longer
        narrated multi-scene videos, use ``POST /v1/workflows/script-to-video``. The generated clip is clamped to the
        selected quality's supported range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.prompt_to_video_clip(body=body, request_options=request_options))

    async def script_to_video(
        self,
        *,
        body: ScriptToVideoRequest | ScriptToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project and generates a narrated video from a prompt or script. Returns immediately with a workflow
        run id; poll or subscribe to webhooks for completion.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.script_to_video(body=body, request_options=request_options))

    async def slideshow_to_video(
        self,
        *,
        body: SlideshowToVideoRequest | SlideshowToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project from an uploaded PDF or PowerPoint file and generates an AI-narrated video walking through
        each slide. Upload the file via ``POST /v1/files/upload`` first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.slideshow_to_video(body=body, request_options=request_options))

    async def voiceover_to_video(
        self,
        *,
        body: VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartWorkflowRunResponse:
        """Creates a project from an uploaded voiceover file and generates a video with matching b-roll. Upload the
        voiceover via the files API first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Workflow run accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.voiceover_to_video(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncWorkflowsWithRawResponse:
        return self._with_raw_response


class WorkflowsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/runs/{workflowRunId}/cancel"),
            path_params=[param[str]("workflowRunId", workflow_run_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WorkflowRun, RawError]:
        """Send a ``GET`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/workflows/runs/{workflowRunId}"),
            path_params=[param[str]("workflowRunId", workflow_run_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WorkflowRun],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_workflow_runs(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WorkflowRunListResponse, RawError]:
        """List workflow runs started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all runs for the team are returned. Cursor-paginated; see the
        `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/workflows/runs"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[WorkflowRunListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def prompt_to_video_clip(
        self,
        *,
        body: PromptToVideoClipRequest | PromptToVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project from a text prompt and generates one short AI video clip (up to 30 seconds). VideoGen first
        generates an opening frame from the prompt (optionally guided by reference images), then animates that frame
        into a video. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion. For a
        standalone clip without an editable project, use ``POST /v1/tools/generate-video-clip`` instead. For longer
        narrated multi-scene videos, use ``POST /v1/workflows/script-to-video``. The generated clip is clamped to the
        selected quality's supported range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/prompt-to-video-clip"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PromptToVideoClipRequest | PromptToVideoClipRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def script_to_video(
        self,
        *,
        body: ScriptToVideoRequest | ScriptToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project and generates a narrated video from a prompt or script. Returns immediately with a workflow
        run id; poll or subscribe to webhooks for completion.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/script-to-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScriptToVideoRequest | ScriptToVideoRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def slideshow_to_video(
        self,
        *,
        body: SlideshowToVideoRequest | SlideshowToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project from an uploaded PDF or PowerPoint file and generates an AI-narrated video walking through
        each slide. Upload the file via ``POST /v1/files/upload`` first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/slideshow-to-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SlideshowToVideoRequest | SlideshowToVideoRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def voiceover_to_video(
        self,
        *,
        body: VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project from an uploaded voiceover file and generates a video with matching b-roll. Upload the
        voiceover via the files API first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/voiceover-to-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWorkflowsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/runs/{workflowRunId}/cancel"),
            path_params=[param[str]("workflowRunId", workflow_run_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_workflow_run(
        self, workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[WorkflowRun, RawError]:
        """Send a ``GET`` request.

        Args:
            workflow_run_id: The workflow run id returned when the workflow was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/workflows/runs/{workflowRunId}"),
            path_params=[param[str]("workflowRunId", workflow_run_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WorkflowRun],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_workflow_runs(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WorkflowRunListResponse, RawError]:
        """List workflow runs started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all runs for the team are returned. Cursor-paginated; see the
        `Pagination </pagination>`__ guide.

        Args:
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            self_only: When true, returns only items created by the API key's owner. When false (default), returns all
                items accessible to the team.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/workflows/runs"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[WorkflowRunListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def prompt_to_video_clip(
        self,
        *,
        body: PromptToVideoClipRequest | PromptToVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project from a text prompt and generates one short AI video clip (up to 30 seconds). VideoGen first
        generates an opening frame from the prompt (optionally guided by reference images), then animates that frame
        into a video. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion. For a
        standalone clip without an editable project, use ``POST /v1/tools/generate-video-clip`` instead. For longer
        narrated multi-scene videos, use ``POST /v1/workflows/script-to-video``. The generated clip is clamped to the
        selected quality's supported range.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/prompt-to-video-clip"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PromptToVideoClipRequest | PromptToVideoClipRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def script_to_video(
        self,
        *,
        body: ScriptToVideoRequest | ScriptToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project and generates a narrated video from a prompt or script. Returns immediately with a workflow
        run id; poll or subscribe to webhooks for completion.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/script-to-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScriptToVideoRequest | ScriptToVideoRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def slideshow_to_video(
        self,
        *,
        body: SlideshowToVideoRequest | SlideshowToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project from an uploaded PDF or PowerPoint file and generates an AI-narrated video walking through
        each slide. Upload the file via ``POST /v1/files/upload`` first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/slideshow-to-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SlideshowToVideoRequest | SlideshowToVideoRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def voiceover_to_video(
        self,
        *,
        body: VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartWorkflowRunResponse, RawError]:
        """Creates a project from an uploaded voiceover file and generates a video with matching b-roll. Upload the
        voiceover via the files API first.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/workflows/voiceover-to-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartWorkflowRunResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
