<!-- Generated file — do not edit; regenerated with the SDK. -->

# Account — operations

Accessor: `client.account` · Source: `videogen/apis/account.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account.get_me

- **Route**: `GET /v1/me`
- **Auth**: `bearer_auth`
- **Signature**: `def get_me(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `MeResponse`
- **Returns (raw)**: `ApiResult[MeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `MeResponse` | `videogen/models/me_response.py` |

