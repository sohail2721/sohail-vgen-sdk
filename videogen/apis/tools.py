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
from ..models.executed_tool import ExecutedTool
from ..models.generate_avatar_request import GenerateAvatarRequest, GenerateAvatarRequestDict
from ..models.generate_image_request import GenerateImageRequest, GenerateImageRequestDict
from ..models.generate_motion_graphic_request import GenerateMotionGraphicRequest, GenerateMotionGraphicRequestDict
from ..models.generate_music_request import GenerateMusicRequest, GenerateMusicRequestDict
from ..models.generate_sound_effect_request import GenerateSoundEffectRequest, GenerateSoundEffectRequestDict
from ..models.generate_video_clip_request import GenerateVideoClipRequest, GenerateVideoClipRequestDict
from ..models.image_asset_request import ImageAssetRequest, ImageAssetRequestDict
from ..models.start_tool_execution_response import StartToolExecutionResponse
from ..models.text_to_speech_request import TextToSpeechRequest, TextToSpeechRequestDict
from ..models.tool_execution_list_response import ToolExecutionListResponse
from ..models.video_asset_request import VideoAssetRequest, VideoAssetRequestDict
from ..server.server import Server


class Tools:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ToolsWithRawResponse(client, server, auth)

    def cancel_tool_execution(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StartToolExecutionResponse:
        """Request cancellation of a running tool execution. The execution transitions to ``cancelled`` if it has not
        already completed.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation request accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.cancel_tool_execution(tool_execution_id, request_options=request_options))

    def generate_avatar(
        self,
        *,
        body: GenerateAvatarRequest | GenerateAvatarRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate a talking-head avatar video by pairing an ACTOR entity with an audio file, typically from a prior
        text-to-speech result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_avatar(body=body, request_options=request_options))

    def generate_image(
        self,
        *,
        body: GenerateImageRequest | GenerateImageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate an image from a text prompt, optionally guided by reference images and actor, product, or
        visual-style entity ids. When reference images are provided, the prompt describes the desired transformation.
        VideoGen automatically routes each request to the most effective state-of-the-art image model for your prompt,
        reference images, entities, and quality tier, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_image(body=body, request_options=request_options))

    def generate_motion_graphic(
        self,
        *,
        body: GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate an animated motion graphic video from a text prompt. This is an experimental, fully agentic
        alternative to a video workflow: VideoGen plans the animation, optionally generates or fetches supporting media,
        and renders a self-contained animated clip. It is especially well suited to precise text animations (e.g. a
        typing effect, animated captions, kinetic typography, lower thirds) that are hard to express with stock or
        generated footage. Optionally pass uploaded ``fileIds`` for reference media and ``entityIds`` for actors,
        products, or visual styles the animation should use. This endpoint returns one standalone video. For longer,
        narrated, multi-scene videos, use a video workflow such as `Script to video </workflows>`__ (``POST
        /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_motion_graphic(body=body, request_options=request_options))

    def generate_music(
        self,
        *,
        body: GenerateMusicRequest | GenerateMusicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate an instrumental music track from a text description. The returned track is approximately 30 seconds
        long. VideoGen automatically routes each request to the most effective state-of-the-art music model for your
        prompt, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_music(body=body, request_options=request_options))

    def generate_sound_effect(
        self,
        *,
        body: GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate a sound effect from a text description. Optionally control the duration and prompt influence.
        VideoGen automatically routes each request to the most effective state-of-the-art sound effect model for your
        prompt and settings, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_sound_effect(body=body, request_options=request_options))

    def generate_video_clip(
        self,
        *,
        body: GenerateVideoClipRequest | GenerateVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate a single short video clip (up to 30 seconds) from a text prompt, optionally guided by an
        opening-frame still, reference images, videos, and audio. At least one of ``prompt``, ``startFrameFileId``,
        ``imageFileIds``, ``videoFileIds``, ``audioFileIds``, or ``spokenDialogue`` must be provided. VideoGen
        automatically routes each request to the most effective state-of-the-art video model for your inputs and
        settings, so you don't pick a model. This endpoint returns one standalone clip. For longer, higher-quality,
        professionally edited videos with narration, captions, music, and multiple scenes, use a video workflow such as
        `Script to video </workflows>`__ (``POST /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.generate_video_clip(body=body, request_options=request_options))

    def get_tool_execution_info(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExecutedTool:
        """Retrieve the current status and result of a tool execution. Poll this endpoint until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``. Each succeeded result carries signed
        ``downloadUrl``/``thumbnailUrl`` (with matching ``*ExpiresAt`` timestamps) alongside the full hydrated ``file``.
        The signed URLs are private and valid for 7 days; this single-execution endpoint automatically re-signs them
        when they are within an hour of expiring, so a caller always receives a URL valid long enough to use. Results
        remain retrievable indefinitely, including executions older than 7 days. Note that list endpoints (e.g. ``GET
        /v1/tools/executions``) do not re-sign URLs: they return the last-signed URL, which may already be expired
        (check ``downloadUrlExpiresAt``). To refresh a URL, GET the individual execution here, or hydrate the file
        directly via ``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Current execution state

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.get_tool_execution_info(tool_execution_id, request_options=request_options)
        )

    def image3d_effect(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Turn a still image into a short video clip with a 3D parallax motion effect, simulating camera movement
        through the scene.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.image3d_effect(body=body, request_options=request_options))

    def list_tool_executions(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ToolExecutionListResponse:
        """List tool executions started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all executions for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide. Executions remain listable indefinitely (including those older than 7
        days). For efficiency this list does not re-sign result download URLs, so ``downloadUrl``/``thumbnailUrl``
        reflect the last time they were signed and may be expired (always check ``downloadUrlExpiresAt``). To obtain a
        fresh signed URL, GET the individual execution (``GET /v1/tools/executions/{toolExecutionId}``) or hydrate the
        file (``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``).

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
            Paginated list of tool executions.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_tool_executions(
                limit=limit, cursor=cursor, self_only=self_only, request_options=request_options
            ),
        )

    def remove_image_background(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Remove the background from an image, returning a transparent-background PNG of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.remove_image_background(body=body, request_options=request_options))

    def remove_video_background(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Remove the background from a video, producing a transparent-background video of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.remove_video_background(body=body, request_options=request_options))

    def text_to_speech(
        self,
        *,
        body: TextToSpeechRequest | TextToSpeechRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Convert text into a spoken audio file. Only voices with ``supportsDirectToolExecution`` set to true can be
        used. Optionally choose a voice, language, speed, and pronunciation overrides.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.text_to_speech(body=body, request_options=request_options))

    def upscale_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Increase the resolution of an image while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.upscale_image(body=body, request_options=request_options))

    def upscale_video(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Increase the resolution of a video while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.upscale_video(body=body, request_options=request_options))

    def vectorize_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Convert any raster image into a scalable vector graphic (SVG). The output traces the shapes and colors of the
        input image.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.vectorize_image(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> ToolsWithRawResponse:
        return self._with_raw_response


class AsyncTools:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncToolsWithRawResponse(client, server, auth)

    async def cancel_tool_execution(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StartToolExecutionResponse:
        """Request cancellation of a running tool execution. The execution transitions to ``cancelled`` if it has not
        already completed.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation request accepted

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_tool_execution(tool_execution_id, request_options=request_options)
        )

    async def generate_avatar(
        self,
        *,
        body: GenerateAvatarRequest | GenerateAvatarRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate a talking-head avatar video by pairing an ACTOR entity with an audio file, typically from a prior
        text-to-speech result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_avatar(body=body, request_options=request_options))

    async def generate_image(
        self,
        *,
        body: GenerateImageRequest | GenerateImageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate an image from a text prompt, optionally guided by reference images and actor, product, or
        visual-style entity ids. When reference images are provided, the prompt describes the desired transformation.
        VideoGen automatically routes each request to the most effective state-of-the-art image model for your prompt,
        reference images, entities, and quality tier, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_image(body=body, request_options=request_options))

    async def generate_motion_graphic(
        self,
        *,
        body: GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate an animated motion graphic video from a text prompt. This is an experimental, fully agentic
        alternative to a video workflow: VideoGen plans the animation, optionally generates or fetches supporting media,
        and renders a self-contained animated clip. It is especially well suited to precise text animations (e.g. a
        typing effect, animated captions, kinetic typography, lower thirds) that are hard to express with stock or
        generated footage. Optionally pass uploaded ``fileIds`` for reference media and ``entityIds`` for actors,
        products, or visual styles the animation should use. This endpoint returns one standalone video. For longer,
        narrated, multi-scene videos, use a video workflow such as `Script to video </workflows>`__ (``POST
        /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_motion_graphic(body=body, request_options=request_options))

    async def generate_music(
        self,
        *,
        body: GenerateMusicRequest | GenerateMusicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate an instrumental music track from a text description. The returned track is approximately 30 seconds
        long. VideoGen automatically routes each request to the most effective state-of-the-art music model for your
        prompt, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_music(body=body, request_options=request_options))

    async def generate_sound_effect(
        self,
        *,
        body: GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate a sound effect from a text description. Optionally control the duration and prompt influence.
        VideoGen automatically routes each request to the most effective state-of-the-art sound effect model for your
        prompt and settings, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_sound_effect(body=body, request_options=request_options))

    async def generate_video_clip(
        self,
        *,
        body: GenerateVideoClipRequest | GenerateVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Generate a single short video clip (up to 30 seconds) from a text prompt, optionally guided by an
        opening-frame still, reference images, videos, and audio. At least one of ``prompt``, ``startFrameFileId``,
        ``imageFileIds``, ``videoFileIds``, ``audioFileIds``, or ``spokenDialogue`` must be provided. VideoGen
        automatically routes each request to the most effective state-of-the-art video model for your inputs and
        settings, so you don't pick a model. This endpoint returns one standalone clip. For longer, higher-quality,
        professionally edited videos with narration, captions, music, and multiple scenes, use a video workflow such as
        `Script to video </workflows>`__ (``POST /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.generate_video_clip(body=body, request_options=request_options))

    async def get_tool_execution_info(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExecutedTool:
        """Retrieve the current status and result of a tool execution. Poll this endpoint until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``. Each succeeded result carries signed
        ``downloadUrl``/``thumbnailUrl`` (with matching ``*ExpiresAt`` timestamps) alongside the full hydrated ``file``.
        The signed URLs are private and valid for 7 days; this single-execution endpoint automatically re-signs them
        when they are within an hour of expiring, so a caller always receives a URL valid long enough to use. Results
        remain retrievable indefinitely, including executions older than 7 days. Note that list endpoints (e.g. ``GET
        /v1/tools/executions``) do not re-sign URLs: they return the last-signed URL, which may already be expired
        (check ``downloadUrlExpiresAt``). To refresh a URL, GET the individual execution here, or hydrate the file
        directly via ``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Current execution state

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_tool_execution_info(tool_execution_id, request_options=request_options)
        )

    async def image3d_effect(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Turn a still image into a short video clip with a 3D parallax motion effect, simulating camera movement
        through the scene.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.image3d_effect(body=body, request_options=request_options))

    async def list_tool_executions(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ToolExecutionListResponse:
        """List tool executions started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all executions for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide. Executions remain listable indefinitely (including those older than 7
        days). For efficiency this list does not re-sign result download URLs, so ``downloadUrl``/``thumbnailUrl``
        reflect the last time they were signed and may be expired (always check ``downloadUrlExpiresAt``). To obtain a
        fresh signed URL, GET the individual execution (``GET /v1/tools/executions/{toolExecutionId}``) or hydrate the
        file (``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``).

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
            Paginated list of tool executions.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_tool_executions(
                limit=limit, cursor=cursor, self_only=self_only, request_options=request_options
            ),
        )

    async def remove_image_background(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Remove the background from an image, returning a transparent-background PNG of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.remove_image_background(body=body, request_options=request_options))

    async def remove_video_background(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Remove the background from a video, producing a transparent-background video of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.remove_video_background(body=body, request_options=request_options))

    async def text_to_speech(
        self,
        *,
        body: TextToSpeechRequest | TextToSpeechRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Convert text into a spoken audio file. Only voices with ``supportsDirectToolExecution`` set to true can be
        used. Optionally choose a voice, language, speed, and pronunciation overrides.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.text_to_speech(body=body, request_options=request_options))

    async def upscale_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Increase the resolution of an image while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.upscale_image(body=body, request_options=request_options))

    async def upscale_video(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Increase the resolution of a video while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.upscale_video(body=body, request_options=request_options))

    async def vectorize_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartToolExecutionResponse:
        """Convert any raster image into a scalable vector graphic (SVG). The output traces the shapes and colors of the
        input image.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Execution accepted; poll until complete.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.vectorize_image(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncToolsWithRawResponse:
        return self._with_raw_response


class ToolsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_tool_execution(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Request cancellation of a running tool execution. The execution transitions to ``cancelled`` if it has not
        already completed.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/executions/{toolExecutionId}/cancel"),
            path_params=[param[str]("toolExecutionId", tool_execution_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_avatar(
        self,
        *,
        body: GenerateAvatarRequest | GenerateAvatarRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate a talking-head avatar video by pairing an ACTOR entity with an audio file, typically from a prior
        text-to-speech result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-avatar"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateAvatarRequest | GenerateAvatarRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_image(
        self,
        *,
        body: GenerateImageRequest | GenerateImageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate an image from a text prompt, optionally guided by reference images and actor, product, or
        visual-style entity ids. When reference images are provided, the prompt describes the desired transformation.
        VideoGen automatically routes each request to the most effective state-of-the-art image model for your prompt,
        reference images, entities, and quality tier, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-image"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateImageRequest | GenerateImageRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_motion_graphic(
        self,
        *,
        body: GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate an animated motion graphic video from a text prompt. This is an experimental, fully agentic
        alternative to a video workflow: VideoGen plans the animation, optionally generates or fetches supporting media,
        and renders a self-contained animated clip. It is especially well suited to precise text animations (e.g. a
        typing effect, animated captions, kinetic typography, lower thirds) that are hard to express with stock or
        generated footage. Optionally pass uploaded ``fileIds`` for reference media and ``entityIds`` for actors,
        products, or visual styles the animation should use. This endpoint returns one standalone video. For longer,
        narrated, multi-scene videos, use a video workflow such as `Script to video </workflows>`__ (``POST
        /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-motion-graphic"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_music(
        self,
        *,
        body: GenerateMusicRequest | GenerateMusicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate an instrumental music track from a text description. The returned track is approximately 30 seconds
        long. VideoGen automatically routes each request to the most effective state-of-the-art music model for your
        prompt, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-music"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateMusicRequest | GenerateMusicRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_sound_effect(
        self,
        *,
        body: GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate a sound effect from a text description. Optionally control the duration and prompt influence.
        VideoGen automatically routes each request to the most effective state-of-the-art sound effect model for your
        prompt and settings, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-sound-effect"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def generate_video_clip(
        self,
        *,
        body: GenerateVideoClipRequest | GenerateVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate a single short video clip (up to 30 seconds) from a text prompt, optionally guided by an
        opening-frame still, reference images, videos, and audio. At least one of ``prompt``, ``startFrameFileId``,
        ``imageFileIds``, ``videoFileIds``, ``audioFileIds``, or ``spokenDialogue`` must be provided. VideoGen
        automatically routes each request to the most effective state-of-the-art video model for your inputs and
        settings, so you don't pick a model. This endpoint returns one standalone clip. For longer, higher-quality,
        professionally edited videos with narration, captions, music, and multiple scenes, use a video workflow such as
        `Script to video </workflows>`__ (``POST /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-video-clip"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateVideoClipRequest | GenerateVideoClipRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_tool_execution_info(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExecutedTool, RawError]:
        """Retrieve the current status and result of a tool execution. Poll this endpoint until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``. Each succeeded result carries signed
        ``downloadUrl``/``thumbnailUrl`` (with matching ``*ExpiresAt`` timestamps) alongside the full hydrated ``file``.
        The signed URLs are private and valid for 7 days; this single-execution endpoint automatically re-signs them
        when they are within an hour of expiring, so a caller always receives a URL valid long enough to use. Results
        remain retrievable indefinitely, including executions older than 7 days. Note that list endpoints (e.g. ``GET
        /v1/tools/executions``) do not re-sign URLs: they return the last-signed URL, which may already be expired
        (check ``downloadUrlExpiresAt``). To refresh a URL, GET the individual execution here, or hydrate the file
        directly via ``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/tools/executions/{toolExecutionId}"),
            path_params=[param[str]("toolExecutionId", tool_execution_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ExecutedTool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def image3d_effect(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Turn a still image into a short video clip with a 3D parallax motion effect, simulating camera movement
        through the scene.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/image-3d-effect"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_tool_executions(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ToolExecutionListResponse, RawError]:
        """List tool executions started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all executions for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide. Executions remain listable indefinitely (including those older than 7
        days). For efficiency this list does not re-sign result download URLs, so ``downloadUrl``/``thumbnailUrl``
        reflect the last time they were signed and may be expired (always check ``downloadUrlExpiresAt``). To obtain a
        fresh signed URL, GET the individual execution (``GET /v1/tools/executions/{toolExecutionId}``) or hydrate the
        file (``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``).

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
            url_template=self._server.default("/v1/tools/executions"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ToolExecutionListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_image_background(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Remove the background from an image, returning a transparent-background PNG of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/remove-image-background"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_video_background(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Remove the background from a video, producing a transparent-background video of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/remove-video-background"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideoAssetRequest | VideoAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def text_to_speech(
        self,
        *,
        body: TextToSpeechRequest | TextToSpeechRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Convert text into a spoken audio file. Only voices with ``supportsDirectToolExecution`` set to true can be
        used. Optionally choose a voice, language, speed, and pronunciation overrides.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/text-to-speech"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TextToSpeechRequest | TextToSpeechRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upscale_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Increase the resolution of an image while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/upscale-image"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upscale_video(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Increase the resolution of a video while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/upscale-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideoAssetRequest | VideoAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def vectorize_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Convert any raster image into a scalable vector graphic (SVG). The output traces the shapes and colors of the
        input image.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/vectorize-image"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncToolsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_tool_execution(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Request cancellation of a running tool execution. The execution transitions to ``cancelled`` if it has not
        already completed.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/executions/{toolExecutionId}/cancel"),
            path_params=[param[str]("toolExecutionId", tool_execution_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_avatar(
        self,
        *,
        body: GenerateAvatarRequest | GenerateAvatarRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate a talking-head avatar video by pairing an ACTOR entity with an audio file, typically from a prior
        text-to-speech result.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-avatar"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateAvatarRequest | GenerateAvatarRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_image(
        self,
        *,
        body: GenerateImageRequest | GenerateImageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate an image from a text prompt, optionally guided by reference images and actor, product, or
        visual-style entity ids. When reference images are provided, the prompt describes the desired transformation.
        VideoGen automatically routes each request to the most effective state-of-the-art image model for your prompt,
        reference images, entities, and quality tier, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-image"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateImageRequest | GenerateImageRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_motion_graphic(
        self,
        *,
        body: GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate an animated motion graphic video from a text prompt. This is an experimental, fully agentic
        alternative to a video workflow: VideoGen plans the animation, optionally generates or fetches supporting media,
        and renders a self-contained animated clip. It is especially well suited to precise text animations (e.g. a
        typing effect, animated captions, kinetic typography, lower thirds) that are hard to express with stock or
        generated footage. Optionally pass uploaded ``fileIds`` for reference media and ``entityIds`` for actors,
        products, or visual styles the animation should use. This endpoint returns one standalone video. For longer,
        narrated, multi-scene videos, use a video workflow such as `Script to video </workflows>`__ (``POST
        /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-motion-graphic"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_music(
        self,
        *,
        body: GenerateMusicRequest | GenerateMusicRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate an instrumental music track from a text description. The returned track is approximately 30 seconds
        long. VideoGen automatically routes each request to the most effective state-of-the-art music model for your
        prompt, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-music"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateMusicRequest | GenerateMusicRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_sound_effect(
        self,
        *,
        body: GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate a sound effect from a text description. Optionally control the duration and prompt influence.
        VideoGen automatically routes each request to the most effective state-of-the-art sound effect model for your
        prompt and settings, so you don't pick a model.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-sound-effect"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def generate_video_clip(
        self,
        *,
        body: GenerateVideoClipRequest | GenerateVideoClipRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Generate a single short video clip (up to 30 seconds) from a text prompt, optionally guided by an
        opening-frame still, reference images, videos, and audio. At least one of ``prompt``, ``startFrameFileId``,
        ``imageFileIds``, ``videoFileIds``, ``audioFileIds``, or ``spokenDialogue`` must be provided. VideoGen
        automatically routes each request to the most effective state-of-the-art video model for your inputs and
        settings, so you don't pick a model. This endpoint returns one standalone clip. For longer, higher-quality,
        professionally edited videos with narration, captions, music, and multiple scenes, use a video workflow such as
        `Script to video </workflows>`__ (``POST /v1/workflows/script-to-video``) instead.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/generate-video-clip"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateVideoClipRequest | GenerateVideoClipRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_tool_execution_info(
        self, tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExecutedTool, RawError]:
        """Retrieve the current status and result of a tool execution. Poll this endpoint until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``. Each succeeded result carries signed
        ``downloadUrl``/``thumbnailUrl`` (with matching ``*ExpiresAt`` timestamps) alongside the full hydrated ``file``.
        The signed URLs are private and valid for 7 days; this single-execution endpoint automatically re-signs them
        when they are within an hour of expiring, so a caller always receives a URL valid long enough to use. Results
        remain retrievable indefinitely, including executions older than 7 days. Note that list endpoints (e.g. ``GET
        /v1/tools/executions``) do not re-sign URLs: they return the last-signed URL, which may already be expired
        (check ``downloadUrlExpiresAt``). To refresh a URL, GET the individual execution here, or hydrate the file
        directly via ``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``.

        Args:
            tool_execution_id: The tool execution id returned when the tool was started.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/tools/executions/{toolExecutionId}"),
            path_params=[param[str]("toolExecutionId", tool_execution_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ExecutedTool],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def image3d_effect(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Turn a still image into a short video clip with a 3D parallax motion effect, simulating camera movement
        through the scene.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/image-3d-effect"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_tool_executions(
        self,
        *,
        limit: int | None = 50,
        cursor: str | None = None,
        self_only: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ToolExecutionListResponse, RawError]:
        """List tool executions started via the API, most recently created first. Use ``selfOnly=true`` to restrict
        results to the calling API key's user; otherwise all executions for the team are returned. Cursor-paginated; see
        the `Pagination </pagination>`__ guide. Executions remain listable indefinitely (including those older than 7
        days). For efficiency this list does not re-sign result download URLs, so ``downloadUrl``/``thumbnailUrl``
        reflect the last time they were signed and may be expired (always check ``downloadUrlExpiresAt``). To obtain a
        fresh signed URL, GET the individual execution (``GET /v1/tools/executions/{toolExecutionId}``) or hydrate the
        file (``GET /v1/files/{fileId}`` / ``POST /v1/files/{fileId}/hydrate``).

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
            url_template=self._server.default("/v1/tools/executions"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[bool | None]("selfOnly", self_only),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ToolExecutionListResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_image_background(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Remove the background from an image, returning a transparent-background PNG of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/remove-image-background"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_video_background(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Remove the background from a video, producing a transparent-background video of the foreground subject.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/remove-video-background"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideoAssetRequest | VideoAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def text_to_speech(
        self,
        *,
        body: TextToSpeechRequest | TextToSpeechRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Convert text into a spoken audio file. Only voices with ``supportsDirectToolExecution`` set to true can be
        used. Optionally choose a voice, language, speed, and pronunciation overrides.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/text-to-speech"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TextToSpeechRequest | TextToSpeechRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upscale_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Increase the resolution of an image while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/upscale-image"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upscale_video(
        self,
        *,
        body: VideoAssetRequest | VideoAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Increase the resolution of a video while preserving detail and sharpness.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/upscale-video"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[VideoAssetRequest | VideoAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def vectorize_image(
        self,
        *,
        body: ImageAssetRequest | ImageAssetRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartToolExecutionResponse, RawError]:
        """Convert any raster image into a scalable vector graphic (SVG). The output traces the shapes and colors of the
        input image.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/tools/vectorize-image"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ImageAssetRequest | ImageAssetRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartToolExecutionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
