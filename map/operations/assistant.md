<!-- Generated file — do not edit; regenerated with the SDK. -->

# Assistant — operations

Accessor: `client.assistant` · Source: `videogen/apis/assistant.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.assistant.act_on_assistant_action

- **Route**: `POST /v1/assistants/{assistantId}/actions/{actionId}`
- **Auth**: `bearer_auth`
- **Signature**: `def act_on_assistant_action(assistant_id: str, action_id: str, *, body: ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `assistant_id`, `action_id`
- **Params**: `assistant_id` — path `assistantId` · `action_id` — path `actionId` · `body` — JSON body
- **Returns (parsed)**: `ActOnAssistantActionResponse`
- **Returns (raw)**: `ApiResult[ActOnAssistantActionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ActOnAssistantActionRequest` | `videogen/models/act_on_assistant_action_request.py` |
| `ActOnAssistantActionRequestDict` | `videogen/models/act_on_assistant_action_request.py` |
| `ActOnAssistantActionResponse` | `videogen/models/act_on_assistant_action_response.py` |

### client.assistant.get_assistant

- **Route**: `GET /v1/assistants/{assistantId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_assistant(assistant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `assistant_id`
- **Params**: `assistant_id` — path `assistantId`
- **Returns (parsed)**: `GetAssistantResponse`
- **Returns (raw)**: `ApiResult[GetAssistantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetAssistantResponse` | `videogen/models/get_assistant_response.py` |

### client.assistant.get_assistant_message

- **Route**: `GET /v1/assistant-messages/{messageId}`
- **Auth**: `bearer_auth`
- **Signature**: `def get_assistant_message(message_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `message_id`
- **Params**: `message_id` — path `messageId`
- **Returns (parsed)**: `AssistantMessage2`
- **Returns (raw)**: `ApiResult[AssistantMessage2, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AssistantMessage2` | `videogen/models/unions/assistant_message2.py` |

### client.assistant.send_assistant_message

- **Route**: `POST /v1/assistants/{assistantId}/messages`
- **Auth**: `bearer_auth`
- **Signature**: `def send_assistant_message(assistant_id: str, *, body: SendAssistantMessageRequest | SendAssistantMessageRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `assistant_id`
- **Params**: `assistant_id` — path `assistantId` · `body` — JSON body
- **Returns (parsed)**: `SendAssistantMessageResponse`
- **Returns (raw)**: `ApiResult[SendAssistantMessageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SendAssistantMessageRequest` | `videogen/models/send_assistant_message_request.py` |
| `SendAssistantMessageRequestDict` | `videogen/models/send_assistant_message_request.py` |
| `SendAssistantMessageResponse` | `videogen/models/send_assistant_message_response.py` |

### client.assistant.start_assistant_chat

- **Route**: `POST /v1/assistants`
- **Auth**: `bearer_auth`
- **Signature**: `def start_assistant_chat(*, body: StartAssistantChatRequest | StartAssistantChatRequestDict | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `StartAssistantChatResponse`
- **Returns (raw)**: `ApiResult[StartAssistantChatResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StartAssistantChatRequest` | `videogen/models/start_assistant_chat_request.py` |
| `StartAssistantChatRequestDict` | `videogen/models/start_assistant_chat_request.py` |
| `StartAssistantChatResponse` | `videogen/models/start_assistant_chat_response.py` |

