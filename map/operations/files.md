<!-- Generated file — do not edit; regenerated with the SDK. -->

# Files — operations

Accessor: `client.files` · Source: `videogen/apis/files.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.files.archive_file

- **Route**: `POST /v1/files/{fileId}/archive`
- **Auth**: `bearer_auth`
- **Signature**: `def archive_file(file_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file_id`
- **Params**: `file_id` — path `fileId`
- **Returns (parsed)**: `FileInfo`
- **Returns (raw)**: `ApiResult[FileInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FileInfo` | `videogen/models/file_info.py` |

### client.files.create_file_upload

- **Route**: `POST /v1/files/upload`
- **Auth**: `bearer_auth`
- **Signature**: `def create_file_upload(*, body: CreateFileUploadRequest | CreateFileUploadRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FileUploadResponse`
- **Returns (raw)**: `ApiResult[FileUploadResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateFileUploadRequest` | `videogen/models/create_file_upload_request.py` |
| `CreateFileUploadRequestDict` | `videogen/models/create_file_upload_request.py` |
| `FileUploadResponse` | `videogen/models/file_upload_response.py` |

### client.files.disable_public_preview

- **Route**: `POST /v1/files/{fileId}/disable-public-preview`
- **Auth**: `bearer_auth`
- **Signature**: `def disable_public_preview(file_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file_id`
- **Params**: `file_id` — path `fileId`
- **Returns (parsed)**: `FileInfo`
- **Returns (raw)**: `ApiResult[FileInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FileInfo` | `videogen/models/file_info.py` |

### client.files.enable_public_preview

- **Route**: `POST /v1/files/{fileId}/enable-public-preview`
- **Auth**: `bearer_auth`
- **Signature**: `def enable_public_preview(file_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file_id`
- **Params**: `file_id` — path `fileId`
- **Returns (parsed)**: `FileInfo`
- **Returns (raw)**: `ApiResult[FileInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FileInfo` | `videogen/models/file_info.py` |

### client.files.get_file

- **Route**: `GET /v1/files/{fileId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_file(file_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file_id`
- **Params**: `file_id` — path `fileId`
- **Returns (parsed)**: `FileInfo`
- **Returns (raw)**: `ApiResult[FileInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FileInfo` | `videogen/models/file_info.py` |

### client.files.get_files

- **Route**: `GET /v1/files`
- **Auth**: `bearer_auth`
- **Signature**: `def get_files(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, include_export_files: bool | None = False, include_project_files: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query · `self_only` — query `selfOnly` · `include_export_files` — query `includeExportFiles` · `include_project_files` — query `includeProjectFiles`
- **Returns (parsed)**: `GetFilesResponse`
- **Returns (raw)**: `ApiResult[GetFilesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetFilesResponse` | `videogen/models/get_files_response.py` |

### client.files.hydrate_file

- **Route**: `POST /v1/files/{fileId}/hydrate`
- **Auth**: `bearer_auth`
- **Signature**: `def hydrate_file(file_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `file_id`
- **Params**: `file_id` — path `fileId`
- **Returns (parsed)**: `FileInfo`
- **Returns (raw)**: `ApiResult[FileInfo, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `FileInfo` | `videogen/models/file_info.py` |

### client.files.search_files

- **Route**: `POST /v1/files/search`
- **Auth**: `bearer_auth`
- **Signature**: `def search_files(*, body: SearchFilesRequest | SearchFilesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchFilesResponse`
- **Returns (raw)**: `ApiResult[SearchFilesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchFilesRequest` | `videogen/models/search_files_request.py` |
| `SearchFilesRequestDict` | `videogen/models/search_files_request.py` |
| `SearchFilesResponse` | `videogen/models/search_files_response.py` |

