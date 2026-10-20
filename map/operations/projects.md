<!-- Generated file — do not edit; regenerated with the SDK. -->

# Projects — operations

Accessor: `client.projects` · Source: `videogen/apis/projects.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.projects.create_timeline_interchange

- **Route**: `POST /v1/projects/{projectId}/timeline-interchange`
- **Auth**: `bearer_auth`
- **Signature**: `def create_timeline_interchange(project_id: str, *, body: CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path `projectId` · `body` — JSON body
- **Returns (parsed)**: `CreateTimelineInterchangeResponse`
- **Returns (raw)**: `ApiResult[CreateTimelineInterchangeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTimelineInterchangeRequest` | `videogen/models/create_timeline_interchange_request.py` |
| `CreateTimelineInterchangeRequestDict` | `videogen/models/create_timeline_interchange_request.py` |
| `CreateTimelineInterchangeResponse` | `videogen/models/create_timeline_interchange_response.py` |

### client.projects.export_project

- **Route**: `POST /v1/projects/{projectId}/export`
- **Auth**: `bearer_auth`
- **Signature**: `def export_project(project_id: str, *, body: ExportProjectRequest | ExportProjectRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path `projectId` · `body` — JSON body
- **Returns (parsed)**: `ExportProjectResponse`
- **Returns (raw)**: `ApiResult[ExportProjectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ExportProjectRequest` | `videogen/models/export_project_request.py` |
| `ExportProjectRequestDict` | `videogen/models/export_project_request.py` |
| `ExportProjectResponse` | `videogen/models/export_project_response.py` |

### client.projects.get_project

- **Route**: `GET /v1/projects/{projectId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_project(project_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path `projectId`
- **Returns (parsed)**: `ProjectResponse`
- **Returns (raw)**: `ApiResult[ProjectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProjectResponse` | `videogen/models/project_response.py` |

### client.projects.get_project_export

- **Route**: `GET /v1/projects/{projectId}/exports/{exportId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_project_export(project_id: str, export_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`, `export_id`
- **Params**: `project_id` — path `projectId` · `export_id` — path `exportId`
- **Returns (parsed)**: `ProjectExport`
- **Returns (raw)**: `ApiResult[ProjectExport, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProjectExport` | `videogen/models/project_export.py` |

### client.projects.get_timeline_interchange

- **Route**: `GET /v1/timeline-interchange/{interchangeJobId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_timeline_interchange(interchange_job_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `interchange_job_id`
- **Params**: `interchange_job_id` — path `interchangeJobId`
- **Returns (parsed)**: `TimelineInterchange`
- **Returns (raw)**: `ApiResult[TimelineInterchange, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TimelineInterchange` | `videogen/models/timeline_interchange.py` |

### client.projects.list_project_exports

- **Route**: `GET /v1/projects/{projectId}/exports`
- **Auth**: `bearer_auth`
- **Signature**: `def list_project_exports(project_id: str, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path `projectId` · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListProjectExportsResponse`
- **Returns (raw)**: `ApiResult[ListProjectExportsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListProjectExportsResponse` | `videogen/models/list_project_exports_response.py` |

### client.projects.list_project_remix_actions

- **Route**: `GET /v1/projects/{projectId}/remix-actions`
- **Auth**: `bearer_auth`
- **Signature**: `def list_project_remix_actions(project_id: str, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path `projectId` · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListRemixActionsResponse`
- **Returns (raw)**: `ApiResult[ListRemixActionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListRemixActionsResponse` | `videogen/models/list_remix_actions_response.py` |

### client.projects.list_projects

- **Route**: `GET /v1/projects`
- **Auth**: `bearer_auth`
- **Signature**: `def list_projects(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, include_ui_projects: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query · `self_only` — query `selfOnly` · `include_ui_projects` — query `includeUiProjects`
- **Returns (parsed)**: `ListProjectsResponse`
- **Returns (raw)**: `ApiResult[ListProjectsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListProjectsResponse` | `videogen/models/list_projects_response.py` |

### client.projects.remix_project

- **Route**: `POST /v1/projects/{projectId}/remix`
- **Auth**: `bearer_auth`
- **Signature**: `def remix_project(project_id: str, *, body: RemixProjectRequest | RemixProjectRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `project_id`
- **Params**: `project_id` — path `projectId` · `body` — JSON body
- **Returns (parsed)**: `RemixProjectResponse`
- **Returns (raw)**: `ApiResult[RemixProjectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RemixProjectRequest` | `videogen/models/remix_project_request.py` |
| `RemixProjectRequestDict` | `videogen/models/remix_project_request.py` |
| `RemixProjectResponse` | `videogen/models/remix_project_response.py` |

