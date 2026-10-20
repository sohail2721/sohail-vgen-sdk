<!-- Generated file — do not edit; regenerated with the SDK. -->

# Tools — operations

Accessor: `client.tools` · Source: `videogen/apis/tools.py` · 16 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.tools.cancel_tool_execution

- **Route**: `POST /v1/tools/executions/{toolExecutionId}/cancel`
- **Auth**: `bearer_auth`
- **Signature**: `def cancel_tool_execution(tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `tool_execution_id`
- **Params**: `tool_execution_id` — path `toolExecutionId`
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.generate_avatar

- **Route**: `POST /v1/tools/generate-avatar`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_avatar(*, body: GenerateAvatarRequest | GenerateAvatarRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateAvatarRequest` | `videogen/models/generate_avatar_request.py` |
| `GenerateAvatarRequestDict` | `videogen/models/generate_avatar_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.generate_image

- **Route**: `POST /v1/tools/generate-image`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_image(*, body: GenerateImageRequest | GenerateImageRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateImageRequest` | `videogen/models/generate_image_request.py` |
| `GenerateImageRequestDict` | `videogen/models/generate_image_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.generate_motion_graphic

- **Route**: `POST /v1/tools/generate-motion-graphic`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_motion_graphic(*, body: GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateMotionGraphicRequest` | `videogen/models/generate_motion_graphic_request.py` |
| `GenerateMotionGraphicRequestDict` | `videogen/models/generate_motion_graphic_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.generate_music

- **Route**: `POST /v1/tools/generate-music`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_music(*, body: GenerateMusicRequest | GenerateMusicRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateMusicRequest` | `videogen/models/generate_music_request.py` |
| `GenerateMusicRequestDict` | `videogen/models/generate_music_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.generate_sound_effect

- **Route**: `POST /v1/tools/generate-sound-effect`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_sound_effect(*, body: GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateSoundEffectRequest` | `videogen/models/generate_sound_effect_request.py` |
| `GenerateSoundEffectRequestDict` | `videogen/models/generate_sound_effect_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.generate_video_clip

- **Route**: `POST /v1/tools/generate-video-clip`
- **Auth**: `bearer_auth`
- **Signature**: `def generate_video_clip(*, body: GenerateVideoClipRequest | GenerateVideoClipRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GenerateVideoClipRequest` | `videogen/models/generate_video_clip_request.py` |
| `GenerateVideoClipRequestDict` | `videogen/models/generate_video_clip_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.get_tool_execution_info

- **Route**: `GET /v1/tools/executions/{toolExecutionId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_tool_execution_info(tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `tool_execution_id`
- **Params**: `tool_execution_id` — path `toolExecutionId`
- **Returns (parsed)**: `ExecutedTool`
- **Returns (raw)**: `ApiResult[ExecutedTool, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ExecutedTool` | `videogen/models/executed_tool.py` |

### client.tools.image3d_effect

- **Route**: `POST /v1/tools/image-3d-effect`
- **Auth**: `bearer_auth`
- **Signature**: `def image3d_effect(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ImageAssetRequest` | `videogen/models/image_asset_request.py` |
| `ImageAssetRequestDict` | `videogen/models/image_asset_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.list_tool_executions

- **Route**: `GET /v1/tools/executions`
- **Auth**: `bearer_auth`
- **Signature**: `def list_tool_executions(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query · `self_only` — query `selfOnly`
- **Returns (parsed)**: `ToolExecutionListResponse`
- **Returns (raw)**: `ApiResult[ToolExecutionListResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ToolExecutionListResponse` | `videogen/models/tool_execution_list_response.py` |

### client.tools.remove_image_background

- **Route**: `POST /v1/tools/remove-image-background`
- **Auth**: `bearer_auth`
- **Signature**: `def remove_image_background(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ImageAssetRequest` | `videogen/models/image_asset_request.py` |
| `ImageAssetRequestDict` | `videogen/models/image_asset_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.remove_video_background

- **Route**: `POST /v1/tools/remove-video-background`
- **Auth**: `bearer_auth`
- **Signature**: `def remove_video_background(*, body: VideoAssetRequest | VideoAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoAssetRequest` | `videogen/models/video_asset_request.py` |
| `VideoAssetRequestDict` | `videogen/models/video_asset_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.text_to_speech

- **Route**: `POST /v1/tools/text-to-speech`
- **Auth**: `bearer_auth`
- **Signature**: `def text_to_speech(*, body: TextToSpeechRequest | TextToSpeechRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TextToSpeechRequest` | `videogen/models/text_to_speech_request.py` |
| `TextToSpeechRequestDict` | `videogen/models/text_to_speech_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.upscale_image

- **Route**: `POST /v1/tools/upscale-image`
- **Auth**: `bearer_auth`
- **Signature**: `def upscale_image(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ImageAssetRequest` | `videogen/models/image_asset_request.py` |
| `ImageAssetRequestDict` | `videogen/models/image_asset_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.upscale_video

- **Route**: `POST /v1/tools/upscale-video`
- **Auth**: `bearer_auth`
- **Signature**: `def upscale_video(*, body: VideoAssetRequest | VideoAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VideoAssetRequest` | `videogen/models/video_asset_request.py` |
| `VideoAssetRequestDict` | `videogen/models/video_asset_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

### client.tools.vectorize_image

- **Route**: `POST /v1/tools/vectorize-image`
- **Auth**: `bearer_auth`
- **Signature**: `def vectorize_image(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartToolExecutionResponse`
- **Returns (raw)**: `ApiResult[StartToolExecutionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ImageAssetRequest` | `videogen/models/image_asset_request.py` |
| `ImageAssetRequestDict` | `videogen/models/image_asset_request.py` |
| `StartToolExecutionResponse` | `videogen/models/start_tool_execution_response.py` |

