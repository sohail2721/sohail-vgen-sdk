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
from ..models.act_on_assistant_action_request import ActOnAssistantActionRequest, ActOnAssistantActionRequestDict
from ..models.act_on_assistant_action_response import ActOnAssistantActionResponse
from ..models.get_assistant_response import GetAssistantResponse
from ..models.send_assistant_message_request import SendAssistantMessageRequest, SendAssistantMessageRequestDict
from ..models.send_assistant_message_response import SendAssistantMessageResponse
from ..models.start_assistant_chat_request import StartAssistantChatRequest, StartAssistantChatRequestDict
from ..models.start_assistant_chat_response import StartAssistantChatResponse
from ..models.unions.assistant_message2 import AssistantMessage2
from ..server.server import Server


class Assistant:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AssistantWithRawResponse(client, server, auth)

    def act_on_assistant_action(
        self,
        assistant_id: str,
        action_id: str,
        *,
        body: ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ActOnAssistantActionResponse:
        """Acts on an actionable widget the assistant offered on a prior turn. Reference the action by its ``actionId``
        from a prior assistant message. ``APPROVE`` (the default) completes the action; ``REJECT`` records the
        rejection. Two kinds are actionable via the API: accepting a workflow suggestion (``APPROVE`` applies the
        suggested workflow and immediately starts generating; the returned assistant message carries the workflow run in
        ``generation``), and applying an assistant edit (an ``APPLY_EDIT`` action with ``requiresApp`` false, which
        applies the edit to the project). Actions with ``requiresApp`` set to true (plans, tools, and other app-only
        widgets) can only be completed in the web app: open the assistant's ``projectUrl`` instead. Asynchronous: the
        response contains the ``messageId`` of the resulting assistant message. Poll ``GET
        /v1/assistant-messages/{messageId}`` for its terminal state.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            action_id: The ``actionId`` of the action to act on, from a prior assistant message.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Assistant action accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.act_on_assistant_action(
                assistant_id, action_id, body=body, request_options=request_options
            ),
        )

    def get_assistant(
        self, assistant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetAssistantResponse:
        """Returns the assistant chat identified by ``assistantId``, including every message in it (user and assistant
        turns) in chronological order.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The assistant chat and its messages.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_assistant(assistant_id, request_options=request_options))

    def get_assistant_message(
        self, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AssistantMessage2:
        """Returns a single assistant chat message by id. Poll after a POST that returned ``messageId`` until ``status``
        is ``succeeded``, ``failed``, or ``cancelled``. Also supported for ``USER`` messages (which reach terminal state
        as soon as they're accepted).

        Args:
            message_id: The assistant message id (e.g. ``vg_mesg_...``) returned by an assistant POST.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The assistant chat message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_assistant_message(message_id, request_options=request_options))

    def send_assistant_message(
        self,
        assistant_id: str,
        *,
        body: SendAssistantMessageRequest | SendAssistantMessageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SendAssistantMessageResponse:
        """Sends a follow-up message to an existing assistant chat started with ``POST /v1/assistants``. Asynchronous:
        the response contains the ``messageId`` of the assistant's pending reply. Poll ``GET
        /v1/assistant-messages/{messageId}`` until ``status`` is terminal, or subscribe to ``assistant_message.*``
        webhooks.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Assistant message accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.send_assistant_message(assistant_id, body=body, request_options=request_options)
        )

    def start_assistant_chat(
        self,
        *,
        body: StartAssistantChatRequest | StartAssistantChatRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartAssistantChatResponse:
        """Creates a new project and sends the first message to the VideoGen AI assistant, exactly like typing into the
        assistant on a new project in the app. Asynchronous: the response contains the ``messageId`` of the assistant's
        pending reply (e.g. ``vg_mesg_...``). Poll ``GET /v1/assistant-messages/{messageId}`` until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``, or subscribe to ``assistant_message.*`` webhooks. Fetch the parent
        assistant with ``GET /v1/assistants/{assistantId}`` to list all messages in the chat.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Assistant message accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.start_assistant_chat(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AssistantWithRawResponse:
        return self._with_raw_response


class AsyncAssistant:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAssistantWithRawResponse(client, server, auth)

    async def act_on_assistant_action(
        self,
        assistant_id: str,
        action_id: str,
        *,
        body: ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ActOnAssistantActionResponse:
        """Acts on an actionable widget the assistant offered on a prior turn. Reference the action by its ``actionId``
        from a prior assistant message. ``APPROVE`` (the default) completes the action; ``REJECT`` records the
        rejection. Two kinds are actionable via the API: accepting a workflow suggestion (``APPROVE`` applies the
        suggested workflow and immediately starts generating; the returned assistant message carries the workflow run in
        ``generation``), and applying an assistant edit (an ``APPLY_EDIT`` action with ``requiresApp`` false, which
        applies the edit to the project). Actions with ``requiresApp`` set to true (plans, tools, and other app-only
        widgets) can only be completed in the web app: open the assistant's ``projectUrl`` instead. Asynchronous: the
        response contains the ``messageId`` of the resulting assistant message. Poll ``GET
        /v1/assistant-messages/{messageId}`` for its terminal state.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            action_id: The ``actionId`` of the action to act on, from a prior assistant message.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Assistant action accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.act_on_assistant_action(
                assistant_id, action_id, body=body, request_options=request_options
            ),
        )

    async def get_assistant(
        self, assistant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetAssistantResponse:
        """Returns the assistant chat identified by ``assistantId``, including every message in it (user and assistant
        turns) in chronological order.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The assistant chat and its messages.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_assistant(assistant_id, request_options=request_options))

    async def get_assistant_message(
        self, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AssistantMessage2:
        """Returns a single assistant chat message by id. Poll after a POST that returned ``messageId`` until ``status``
        is ``succeeded``, ``failed``, or ``cancelled``. Also supported for ``USER`` messages (which reach terminal state
        as soon as they're accepted).

        Args:
            message_id: The assistant message id (e.g. ``vg_mesg_...``) returned by an assistant POST.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The assistant chat message.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_assistant_message(message_id, request_options=request_options))

    async def send_assistant_message(
        self,
        assistant_id: str,
        *,
        body: SendAssistantMessageRequest | SendAssistantMessageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SendAssistantMessageResponse:
        """Sends a follow-up message to an existing assistant chat started with ``POST /v1/assistants``. Asynchronous:
        the response contains the ``messageId`` of the assistant's pending reply. Poll ``GET
        /v1/assistant-messages/{messageId}`` until ``status`` is terminal, or subscribe to ``assistant_message.*``
        webhooks.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Assistant message accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.send_assistant_message(
                assistant_id, body=body, request_options=request_options
            ),
        )

    async def start_assistant_chat(
        self,
        *,
        body: StartAssistantChatRequest | StartAssistantChatRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartAssistantChatResponse:
        """Creates a new project and sends the first message to the VideoGen AI assistant, exactly like typing into the
        assistant on a new project in the app. Asynchronous: the response contains the ``messageId`` of the assistant's
        pending reply (e.g. ``vg_mesg_...``). Poll ``GET /v1/assistant-messages/{messageId}`` until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``, or subscribe to ``assistant_message.*`` webhooks. Fetch the parent
        assistant with ``GET /v1/assistants/{assistantId}`` to list all messages in the chat.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Assistant message accepted.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.start_assistant_chat(body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAssistantWithRawResponse:
        return self._with_raw_response


class AssistantWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def act_on_assistant_action(
        self,
        assistant_id: str,
        action_id: str,
        *,
        body: ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ActOnAssistantActionResponse, RawError]:
        """Acts on an actionable widget the assistant offered on a prior turn. Reference the action by its ``actionId``
        from a prior assistant message. ``APPROVE`` (the default) completes the action; ``REJECT`` records the
        rejection. Two kinds are actionable via the API: accepting a workflow suggestion (``APPROVE`` applies the
        suggested workflow and immediately starts generating; the returned assistant message carries the workflow run in
        ``generation``), and applying an assistant edit (an ``APPLY_EDIT`` action with ``requiresApp`` false, which
        applies the edit to the project). Actions with ``requiresApp`` set to true (plans, tools, and other app-only
        widgets) can only be completed in the web app: open the assistant's ``projectUrl`` instead. Asynchronous: the
        response contains the ``messageId`` of the resulting assistant message. Poll ``GET
        /v1/assistant-messages/{messageId}`` for its terminal state.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            action_id: The ``actionId`` of the action to act on, from a prior assistant message.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/assistants/{assistantId}/actions/{actionId}"),
            path_params=[param[str]("assistantId", assistant_id), param[str]("actionId", action_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ActOnAssistantActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_assistant(
        self, assistant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAssistantResponse, RawError]:
        """Returns the assistant chat identified by ``assistantId``, including every message in it (user and assistant
        turns) in chronological order.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/assistants/{assistantId}"),
            path_params=[param[str]("assistantId", assistant_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[GetAssistantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_assistant_message(
        self, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AssistantMessage2, RawError]:
        """Returns a single assistant chat message by id. Poll after a POST that returned ``messageId`` until ``status``
        is ``succeeded``, ``failed``, or ``cancelled``. Also supported for ``USER`` messages (which reach terminal state
        as soon as they're accepted).

        Args:
            message_id: The assistant message id (e.g. ``vg_mesg_...``) returned by an assistant POST.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/assistant-messages/{messageId}"),
            path_params=[param[str]("messageId", message_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[AssistantMessage2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def send_assistant_message(
        self,
        assistant_id: str,
        *,
        body: SendAssistantMessageRequest | SendAssistantMessageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SendAssistantMessageResponse, RawError]:
        """Sends a follow-up message to an existing assistant chat started with ``POST /v1/assistants``. Asynchronous:
        the response contains the ``messageId`` of the assistant's pending reply. Poll ``GET
        /v1/assistant-messages/{messageId}`` until ``status`` is terminal, or subscribe to ``assistant_message.*``
        webhooks.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/assistants/{assistantId}/messages"),
            path_params=[param[str]("assistantId", assistant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SendAssistantMessageRequest | SendAssistantMessageRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[SendAssistantMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def start_assistant_chat(
        self,
        *,
        body: StartAssistantChatRequest | StartAssistantChatRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartAssistantChatResponse, RawError]:
        """Creates a new project and sends the first message to the VideoGen AI assistant, exactly like typing into the
        assistant on a new project in the app. Asynchronous: the response contains the ``messageId`` of the assistant's
        pending reply (e.g. ``vg_mesg_...``). Poll ``GET /v1/assistant-messages/{messageId}`` until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``, or subscribe to ``assistant_message.*`` webhooks. Fetch the parent
        assistant with ``GET /v1/assistants/{assistantId}`` to list all messages in the chat.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/assistants"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StartAssistantChatRequest | StartAssistantChatRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[StartAssistantChatResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncAssistantWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def act_on_assistant_action(
        self,
        assistant_id: str,
        action_id: str,
        *,
        body: ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ActOnAssistantActionResponse, RawError]:
        """Acts on an actionable widget the assistant offered on a prior turn. Reference the action by its ``actionId``
        from a prior assistant message. ``APPROVE`` (the default) completes the action; ``REJECT`` records the
        rejection. Two kinds are actionable via the API: accepting a workflow suggestion (``APPROVE`` applies the
        suggested workflow and immediately starts generating; the returned assistant message carries the workflow run in
        ``generation``), and applying an assistant edit (an ``APPLY_EDIT`` action with ``requiresApp`` false, which
        applies the edit to the project). Actions with ``requiresApp`` set to true (plans, tools, and other app-only
        widgets) can only be completed in the web app: open the assistant's ``projectUrl`` instead. Asynchronous: the
        response contains the ``messageId`` of the resulting assistant message. Poll ``GET
        /v1/assistant-messages/{messageId}`` for its terminal state.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            action_id: The ``actionId`` of the action to act on, from a prior assistant message.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/assistants/{assistantId}/actions/{actionId}"),
            path_params=[param[str]("assistantId", assistant_id), param[str]("actionId", action_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ActOnAssistantActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_assistant(
        self, assistant_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAssistantResponse, RawError]:
        """Returns the assistant chat identified by ``assistantId``, including every message in it (user and assistant
        turns) in chronological order.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/assistants/{assistantId}"),
            path_params=[param[str]("assistantId", assistant_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[GetAssistantResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_assistant_message(
        self, message_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AssistantMessage2, RawError]:
        """Returns a single assistant chat message by id. Poll after a POST that returned ``messageId`` until ``status``
        is ``succeeded``, ``failed``, or ``cancelled``. Also supported for ``USER`` messages (which reach terminal state
        as soon as they're accepted).

        Args:
            message_id: The assistant message id (e.g. ``vg_mesg_...``) returned by an assistant POST.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/assistant-messages/{messageId}"),
            path_params=[param[str]("messageId", message_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[AssistantMessage2],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def send_assistant_message(
        self,
        assistant_id: str,
        *,
        body: SendAssistantMessageRequest | SendAssistantMessageRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SendAssistantMessageResponse, RawError]:
        """Sends a follow-up message to an existing assistant chat started with ``POST /v1/assistants``. Asynchronous:
        the response contains the ``messageId`` of the assistant's pending reply. Poll ``GET
        /v1/assistant-messages/{messageId}`` until ``status`` is terminal, or subscribe to ``assistant_message.*``
        webhooks.

        Args:
            assistant_id: The assistant chat id (e.g. ``vg_asst_...``). Every API project has one assistant chat; find
                it on ``ProjectResponse.assistantId``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/assistants/{assistantId}/messages"),
            path_params=[param[str]("assistantId", assistant_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SendAssistantMessageRequest | SendAssistantMessageRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[SendAssistantMessageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def start_assistant_chat(
        self,
        *,
        body: StartAssistantChatRequest | StartAssistantChatRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartAssistantChatResponse, RawError]:
        """Creates a new project and sends the first message to the VideoGen AI assistant, exactly like typing into the
        assistant on a new project in the app. Asynchronous: the response contains the ``messageId`` of the assistant's
        pending reply (e.g. ``vg_mesg_...``). Poll ``GET /v1/assistant-messages/{messageId}`` until ``status`` is
        ``succeeded``, ``failed``, or ``cancelled``, or subscribe to ``assistant_message.*`` webhooks. Fetch the parent
        assistant with ``GET /v1/assistants/{assistantId}`` to list all messages in the chat.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/assistants"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StartAssistantChatRequest | StartAssistantChatRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[StartAssistantChatResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
