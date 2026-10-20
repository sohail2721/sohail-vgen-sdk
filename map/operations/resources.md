<!-- Generated file — do not edit; regenerated with the SDK. -->

# Resources — operations

Accessor: `client.resources` · Source: `videogen/apis/resources.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.resources.list_languages

- **Route**: `GET /v1/resources/languages`
- **Auth**: `bearer_auth`
- **Signature**: `def list_languages(*, query: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `query` — query
- **Returns (parsed)**: `LanguageListResponse`
- **Returns (raw)**: `ApiResult[LanguageListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LanguageListResponse` | `videogen/models/language_list_response.py` |

### client.resources.list_tts_voices

- **Route**: `GET /v1/resources/tts-voices`
- **Auth**: `bearer_auth`
- **Signature**: `def list_tts_voices(*, limit: int | None = 50, cursor: str | None = None, include_deprecated_voices: bool | None = False, query: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query · `include_deprecated_voices` — query `includeDeprecatedVoices` · `query` — query
- **Returns (parsed)**: `TtsVoiceListResponse`
- **Returns (raw)**: `ApiResult[TtsVoiceListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TtsVoiceListResponse` | `videogen/models/tts_voice_list_response.py` |

