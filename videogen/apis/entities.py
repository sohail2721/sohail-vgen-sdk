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
from ..models.add_entity_reference_request import AddEntityReferenceRequest, AddEntityReferenceRequestDict
from ..models.create_entity_request import CreateEntityRequest, CreateEntityRequestDict
from ..models.entity import Entity
from ..models.entity_archive_response import EntityArchiveResponse
from ..models.enums.v1_entities_get_parameters_entity_type import V1EntitiesGetParametersEntityTypeOrStr
from ..models.list_entities_response import ListEntitiesResponse
from ..models.remove_entity_reference_request import RemoveEntityReferenceRequest, RemoveEntityReferenceRequestDict
from ..models.update_entity_request import UpdateEntityRequest, UpdateEntityRequestDict
from ..server.server import Server


class Entities:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EntitiesWithRawResponse(client, server, auth)

    def add_entity_reference(
        self,
        entity_id: str,
        *,
        body: AddEntityReferenceRequest | AddEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Attach an image file as a reference for the entity. Upload the image first via ``POST /v1/files/upload``.
        Returns the updated entity. Built-in entities (``isBuiltIn: true``) cannot have references added.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.add_entity_reference(entity_id, body=body, request_options=request_options)
        )

    def archive_entity(
        self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EntityArchiveResponse:
        """Archive an entity. Archived entities no longer appear in ``GET /v1/entities`` and can't be attached to new
        workflows. Built-in entities (``isBuiltIn: true``) cannot be archived.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Archive acknowledged

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.archive_entity(entity_id, request_options=request_options))

    def create_entity(
        self,
        *,
        body: CreateEntityRequest | CreateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Create a new actor or visual style. Attach reference images with ``POST /v1/entities/{entityId}/references``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The created entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_entity(body=body, request_options=request_options))

    def get_entity(self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Entity:
        """Retrieve a single entity by its id, including its reference images. Built-in catalog entities are included.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_entity(entity_id, request_options=request_options))

    def list_entities(
        self,
        *,
        entity_type: V1EntitiesGetParametersEntityTypeOrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEntitiesResponse:
        """List built-in actors, products, visual styles, and slideshow themes, followed by the entities available to
        your team. Built-in entities have ``isBuiltIn: true`` and cannot be updated or archived. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            entity_type: When provided, returns only entities of this type. Omit to return all entities.
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Entity list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_entities(
                entity_type=entity_type, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    def remove_entity_reference(
        self,
        entity_id: str,
        *,
        body: RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Detach a reference image from the entity. Returns the updated entity. Built-in entities (``isBuiltIn: true``)
        cannot have references removed.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.remove_entity_reference(entity_id, body=body, request_options=request_options)
        )

    def update_entity(
        self,
        entity_id: str,
        *,
        body: UpdateEntityRequest | UpdateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Update an entity's name or description. Provide at least one field. Built-in entities (``isBuiltIn: true``)
        cannot be updated.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.update_entity(entity_id, body=body, request_options=request_options))

    @property
    def with_raw_response(self) -> EntitiesWithRawResponse:
        return self._with_raw_response


class AsyncEntities:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEntitiesWithRawResponse(client, server, auth)

    async def add_entity_reference(
        self,
        entity_id: str,
        *,
        body: AddEntityReferenceRequest | AddEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Attach an image file as a reference for the entity. Upload the image first via ``POST /v1/files/upload``.
        Returns the updated entity. Built-in entities (``isBuiltIn: true``) cannot have references added.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.add_entity_reference(entity_id, body=body, request_options=request_options)
        )

    async def archive_entity(
        self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> EntityArchiveResponse:
        """Archive an entity. Archived entities no longer appear in ``GET /v1/entities`` and can't be attached to new
        workflows. Built-in entities (``isBuiltIn: true``) cannot be archived.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Archive acknowledged

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.archive_entity(entity_id, request_options=request_options))

    async def create_entity(
        self,
        *,
        body: CreateEntityRequest | CreateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Create a new actor or visual style. Attach reference images with ``POST /v1/entities/{entityId}/references``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The created entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_entity(body=body, request_options=request_options))

    async def get_entity(self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Entity:
        """Retrieve a single entity by its id, including its reference images. Built-in catalog entities are included.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_entity(entity_id, request_options=request_options))

    async def list_entities(
        self,
        *,
        entity_type: V1EntitiesGetParametersEntityTypeOrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEntitiesResponse:
        """List built-in actors, products, visual styles, and slideshow themes, followed by the entities available to
        your team. Built-in entities have ``isBuiltIn: true`` and cannot be updated or archived. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            entity_type: When provided, returns only entities of this type. Omit to return all entities.
            limit: Maximum number of items to return in the page. Defaults to 50; capped at 200. See `Pagination
                </pagination>`__.
            cursor: Opaque pagination cursor returned as ``nextCursor`` by the previous page. Omit on the first request.
                Cursors are tied to the endpoint that produced them and must be passed unmodified. See `Pagination
                </pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Entity list

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_entities(
                entity_type=entity_type, limit=limit, cursor=cursor, request_options=request_options
            ),
        )

    async def remove_entity_reference(
        self,
        entity_id: str,
        *,
        body: RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Detach a reference image from the entity. Returns the updated entity. Built-in entities (``isBuiltIn: true``)
        cannot have references removed.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.remove_entity_reference(entity_id, body=body, request_options=request_options)
        )

    async def update_entity(
        self,
        entity_id: str,
        *,
        body: UpdateEntityRequest | UpdateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Entity:
        """Update an entity's name or description. Provide at least one field. Built-in entities (``isBuiltIn: true``)
        cannot be updated.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            The updated entity

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_entity(entity_id, body=body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncEntitiesWithRawResponse:
        return self._with_raw_response


class EntitiesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_entity_reference(
        self,
        entity_id: str,
        *,
        body: AddEntityReferenceRequest | AddEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Attach an image file as a reference for the entity. Upload the image first via ``POST /v1/files/upload``.
        Returns the updated entity. Built-in entities (``isBuiltIn: true``) cannot have references added.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/references"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddEntityReferenceRequest | AddEntityReferenceRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def archive_entity(
        self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EntityArchiveResponse, RawError]:
        """Archive an entity. Archived entities no longer appear in ``GET /v1/entities`` and can't be attached to new
        workflows. Built-in entities (``isBuiltIn: true``) cannot be archived.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/archive"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[EntityArchiveResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_entity(
        self,
        *,
        body: CreateEntityRequest | CreateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Create a new actor or visual style. Attach reference images with ``POST /v1/entities/{entityId}/references``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateEntityRequest | CreateEntityRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_entity(
        self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Entity, RawError]:
        """Retrieve a single entity by its id, including its reference images. Built-in catalog entities are included.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/entities/{entityId}"),
            path_params=[param[str]("entityId", entity_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_entities(
        self,
        *,
        entity_type: V1EntitiesGetParametersEntityTypeOrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEntitiesResponse, RawError]:
        """List built-in actors, products, visual styles, and slideshow themes, followed by the entities available to
        your team. Built-in entities have ``isBuiltIn: true`` and cannot be updated or archived. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            entity_type: When provided, returns only entities of this type. Omit to return all entities.
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
            url_template=self._server.default("/v1/entities"),
            query_params=[
                param[V1EntitiesGetParametersEntityTypeOrStr | None]("entityType", entity_type),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[ListEntitiesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_entity_reference(
        self,
        entity_id: str,
        *,
        body: RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Detach a reference image from the entity. Returns the updated entity. Built-in entities (``isBuiltIn: true``)
        cannot have references removed.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/references/remove"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_entity(
        self,
        entity_id: str,
        *,
        body: UpdateEntityRequest | UpdateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Update an entity's name or description. Provide at least one field. Built-in entities (``isBuiltIn: true``)
        cannot be updated.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/update"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateEntityRequest | UpdateEntityRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEntitiesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_entity_reference(
        self,
        entity_id: str,
        *,
        body: AddEntityReferenceRequest | AddEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Attach an image file as a reference for the entity. Upload the image first via ``POST /v1/files/upload``.
        Returns the updated entity. Built-in entities (``isBuiltIn: true``) cannot have references added.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/references"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AddEntityReferenceRequest | AddEntityReferenceRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def archive_entity(
        self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EntityArchiveResponse, RawError]:
        """Archive an entity. Archived entities no longer appear in ``GET /v1/entities`` and can't be attached to new
        workflows. Built-in entities (``isBuiltIn: true``) cannot be archived.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/archive"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[EntityArchiveResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_entity(
        self,
        *,
        body: CreateEntityRequest | CreateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Create a new actor or visual style. Attach reference images with ``POST /v1/entities/{entityId}/references``.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateEntityRequest | CreateEntityRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_entity(
        self, entity_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Entity, RawError]:
        """Retrieve a single entity by its id, including its reference images. Built-in catalog entities are included.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/entities/{entityId}"),
            path_params=[param[str]("entityId", entity_id)],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_entities(
        self,
        *,
        entity_type: V1EntitiesGetParametersEntityTypeOrStr | None = None,
        limit: int | None = 50,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEntitiesResponse, RawError]:
        """List built-in actors, products, visual styles, and slideshow themes, followed by the entities available to
        your team. Built-in entities have ``isBuiltIn: true`` and cannot be updated or archived. Cursor-paginated; see
        the `Pagination </pagination>`__ guide.

        Args:
            entity_type: When provided, returns only entities of this type. Omit to return all entities.
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
            url_template=self._server.default("/v1/entities"),
            query_params=[
                param[V1EntitiesGetParametersEntityTypeOrStr | None]("entityType", entity_type),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[ListEntitiesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_entity_reference(
        self,
        entity_id: str,
        *,
        body: RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Detach a reference image from the entity. Returns the updated entity. Built-in entities (``isBuiltIn: true``)
        cannot have references removed.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/references/remove"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_entity(
        self,
        entity_id: str,
        *,
        body: UpdateEntityRequest | UpdateEntityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Entity, RawError]:
        """Update an entity's name or description. Provide at least one field. Built-in entities (``isBuiltIn: true``)
        cannot be updated.

        Args:
            entity_id: The entity id (e.g. ``vg_enti_...``).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v1/entities/{entityId}/update"),
            path_params=[param[str]("entityId", entity_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateEntityRequest | UpdateEntityRequestDict | None](body),
            auth_scheme=self._auth.bearer_auth,
            decoder=async_json_decoder[Entity],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
