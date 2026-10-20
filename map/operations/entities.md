<!-- Generated file — do not edit; regenerated with the SDK. -->

# Entities — operations

Accessor: `client.entities` · Source: `videogen/apis/entities.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.entities.add_entity_reference

- **Route**: `POST /v1/entities/{entityId}/references`
- **Auth**: `bearer_auth`
- **Signature**: `def add_entity_reference(entity_id: str, *, body: AddEntityReferenceRequest | AddEntityReferenceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity_id`
- **Params**: `entity_id` — path `entityId` · `body` — JSON body
- **Returns (parsed)**: `Entity`
- **Returns (raw)**: `ApiResult[Entity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddEntityReferenceRequest` | `videogen/models/add_entity_reference_request.py` |
| `AddEntityReferenceRequestDict` | `videogen/models/add_entity_reference_request.py` |
| `Entity` | `videogen/models/entity.py` |

### client.entities.archive_entity

- **Route**: `POST /v1/entities/{entityId}/archive`
- **Auth**: `bearer_auth`
- **Signature**: `def archive_entity(entity_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity_id`
- **Params**: `entity_id` — path `entityId`
- **Returns (parsed)**: `EntityArchiveResponse`
- **Returns (raw)**: `ApiResult[EntityArchiveResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EntityArchiveResponse` | `videogen/models/entity_archive_response.py` |

### client.entities.create_entity

- **Route**: `POST /v1/entities`
- **Auth**: `bearer_auth`
- **Signature**: `def create_entity(*, body: CreateEntityRequest | CreateEntityRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Entity`
- **Returns (raw)**: `ApiResult[Entity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateEntityRequest` | `videogen/models/create_entity_request.py` |
| `CreateEntityRequestDict` | `videogen/models/create_entity_request.py` |
| `Entity` | `videogen/models/entity.py` |

### client.entities.get_entity

- **Route**: `GET /v1/entities/{entityId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_entity(entity_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity_id`
- **Params**: `entity_id` — path `entityId`
- **Returns (parsed)**: `Entity`
- **Returns (raw)**: `ApiResult[Entity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `Entity` | `videogen/models/entity.py` |

### client.entities.list_entities

- **Route**: `GET /v1/entities`
- **Auth**: `bearer_auth`
- **Signature**: `def list_entities(*, entity_type: V1EntitiesGetParametersEntityTypeOrStr | None = None, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `entity_type` — query `entityType` · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListEntitiesResponse`
- **Returns (raw)**: `ApiResult[ListEntitiesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V1EntitiesGetParametersEntityTypeOrStr` | `videogen/models/enums/v1_entities_get_parameters_entity_type.py` |
| `ListEntitiesResponse` | `videogen/models/list_entities_response.py` |

### client.entities.remove_entity_reference

- **Route**: `POST /v1/entities/{entityId}/references/remove`
- **Auth**: `bearer_auth`
- **Signature**: `def remove_entity_reference(entity_id: str, *, body: RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity_id`
- **Params**: `entity_id` — path `entityId` · `body` — JSON body
- **Returns (parsed)**: `Entity`
- **Returns (raw)**: `ApiResult[Entity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RemoveEntityReferenceRequest` | `videogen/models/remove_entity_reference_request.py` |
| `RemoveEntityReferenceRequestDict` | `videogen/models/remove_entity_reference_request.py` |
| `Entity` | `videogen/models/entity.py` |

### client.entities.update_entity

- **Route**: `POST /v1/entities/{entityId}/update`
- **Auth**: `bearer_auth`
- **Signature**: `def update_entity(entity_id: str, *, body: UpdateEntityRequest | UpdateEntityRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `entity_id`
- **Params**: `entity_id` — path `entityId` · `body` — JSON body
- **Returns (parsed)**: `Entity`
- **Returns (raw)**: `ApiResult[Entity, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateEntityRequest` | `videogen/models/update_entity_request.py` |
| `UpdateEntityRequestDict` | `videogen/models/update_entity_request.py` |
| `Entity` | `videogen/models/entity.py` |

