<!-- Generated file — do not edit; regenerated with the SDK. -->

# Webhooks — operations

Accessor: `client.webhooks` · Source: `videogen/apis/webhooks.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded, and an operation with no table mentions nothing but builtins and those.

### client.webhooks.create_webhook_endpoint

- **Route**: `POST /v1/webhooks/endpoints`
- **Auth**: `bearer_auth`
- **Signature**: `def create_webhook_endpoint(*, body: CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `WebhookEndpoint`
- **Returns (raw)**: `ApiResult[WebhookEndpoint, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateWebhookEndpointRequest` | `videogen/models/create_webhook_endpoint_request.py` |
| `CreateWebhookEndpointRequestDict` | `videogen/models/create_webhook_endpoint_request.py` |
| `WebhookEndpoint` | `videogen/models/webhook_endpoint.py` |

### client.webhooks.delete_webhook_endpoint

- **Route**: `DELETE /v1/webhooks/endpoints/{endpointId}`
- **Auth**: `bearer_auth`
- **Signature**: `def delete_webhook_endpoint(endpoint_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `endpoint_id`
- **Params**: `endpoint_id` — path `endpointId`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, RawError]`
- **Error**: `RawError` — **Case B**

### client.webhooks.list_webhook_endpoints

- **Route**: `GET /v1/webhooks/endpoints`
- **Auth**: `bearer_auth`
- **Signature**: `def list_webhook_endpoints(*, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query
- **Returns (parsed)**: `WebhookEndpointListResponse`
- **Returns (raw)**: `ApiResult[WebhookEndpointListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WebhookEndpointListResponse` | `videogen/models/webhook_endpoint_list_response.py` |

