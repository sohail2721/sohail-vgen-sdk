<!-- Generated file — do not edit; regenerated with the SDK. -->

# Workflows — operations

Accessor: `client.workflows` · Source: `videogen/apis/workflows.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.workflows.cancel_workflow_run

- **Route**: `POST /v1/workflows/runs/{workflowRunId}/cancel`
- **Auth**: `bearer_auth`
- **Signature**: `def cancel_workflow_run(workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workflow_run_id`
- **Params**: `workflow_run_id` — path `workflowRunId`
- **Returns (parsed)**: `StartWorkflowRunResponse`
- **Returns (raw)**: `ApiResult[StartWorkflowRunResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StartWorkflowRunResponse` | `videogen/models/start_workflow_run_response.py` |

### client.workflows.get_workflow_run

- **Route**: `GET /v1/workflows/runs/{workflowRunId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_workflow_run(workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `workflow_run_id`
- **Params**: `workflow_run_id` — path `workflowRunId`
- **Returns (parsed)**: `WorkflowRun`
- **Returns (raw)**: `ApiResult[WorkflowRun, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WorkflowRun` | `videogen/models/workflow_run.py` |

### client.workflows.list_workflow_runs

- **Route**: `GET /v1/workflows/runs`
- **Auth**: `bearer_auth`
- **Signature**: `def list_workflow_runs(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query · `self_only` — query `selfOnly`
- **Returns (parsed)**: `WorkflowRunListResponse`
- **Returns (raw)**: `ApiResult[WorkflowRunListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `WorkflowRunListResponse` | `videogen/models/workflow_run_list_response.py` |

### client.workflows.prompt_to_video_clip

- **Route**: `POST /v1/workflows/prompt-to-video-clip`
- **Auth**: `bearer_auth`
- **Signature**: `def prompt_to_video_clip(*, body: PromptToVideoClipRequest | PromptToVideoClipRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartWorkflowRunResponse`
- **Returns (raw)**: `ApiResult[StartWorkflowRunResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PromptToVideoClipRequest` | `videogen/models/prompt_to_video_clip_request.py` |
| `PromptToVideoClipRequestDict` | `videogen/models/prompt_to_video_clip_request.py` |
| `StartWorkflowRunResponse` | `videogen/models/start_workflow_run_response.py` |

### client.workflows.script_to_video

- **Route**: `POST /v1/workflows/script-to-video`
- **Auth**: `bearer_auth`
- **Signature**: `def script_to_video(*, body: ScriptToVideoRequest | ScriptToVideoRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartWorkflowRunResponse`
- **Returns (raw)**: `ApiResult[StartWorkflowRunResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ScriptToVideoRequest` | `videogen/models/script_to_video_request.py` |
| `ScriptToVideoRequestDict` | `videogen/models/script_to_video_request.py` |
| `StartWorkflowRunResponse` | `videogen/models/start_workflow_run_response.py` |

### client.workflows.slideshow_to_video

- **Route**: `POST /v1/workflows/slideshow-to-video`
- **Auth**: `bearer_auth`
- **Signature**: `def slideshow_to_video(*, body: SlideshowToVideoRequest | SlideshowToVideoRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartWorkflowRunResponse`
- **Returns (raw)**: `ApiResult[StartWorkflowRunResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SlideshowToVideoRequest` | `videogen/models/slideshow_to_video_request.py` |
| `SlideshowToVideoRequestDict` | `videogen/models/slideshow_to_video_request.py` |
| `StartWorkflowRunResponse` | `videogen/models/start_workflow_run_response.py` |

### client.workflows.voiceover_to_video

- **Route**: `POST /v1/workflows/voiceover-to-video`
- **Auth**: `bearer_auth`
- **Signature**: `def voiceover_to_video(*, body: VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartWorkflowRunResponse`
- **Returns (raw)**: `ApiResult[StartWorkflowRunResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VoiceoverToVideoRequest` | `videogen/models/voiceover_to_video_request.py` |
| `VoiceoverToVideoRequestDict` | `videogen/models/voiceover_to_video_request.py` |
| `StartWorkflowRunResponse` | `videogen/models/start_workflow_run_response.py` |

