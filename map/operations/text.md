<!-- Generated file — do not edit; regenerated with the SDK. -->

# Text — operations

Accessor: `client.text` · Source: `videogen/apis/text.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.text.generate_text

- **Route**: `POST /v1/text/generate`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_text(*, body: GenerateTextRequest | GenerateTextRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenerateTextResponse`
- **Returns (raw)**: `ApiResult[GenerateTextResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateTextRequest` | `videogen/models/generate_text_request.py` |
| `GenerateTextRequestDict` | `videogen/models/generate_text_request.py` |
| `GenerateTextResponse` | `videogen/models/generate_text_response.py` |

