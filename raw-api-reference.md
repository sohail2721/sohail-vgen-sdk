# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [VideogenClient](videogen/client.py)

## Account

> Source: [Account](videogen/apis/account.py)

<details>
<summary><code>def get_me(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Return the account and team behind the API key making the request. Takes no parameters. Call it as a connection test to confirm a key is valid and to discover the `teamId` and account `email` a key belongs to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account.with_raw_response.get_me()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.account.with_raw_response.get_me()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[MeResponse](videogen/models/me_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[MeResponse](videogen/models/me_response.py)</code> -- The account and team for the authenticated API key.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Assistant

> Source: [Assistant](videogen/apis/assistant.py)

<details>
<summary><code>def act_on_assistant_action(assistant_id: str, action_id: str, *, body: ActOnAssistantActionRequest | ActOnAssistantActionRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ActOnAssistantActionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Acts on an actionable widget the assistant offered on a prior turn. Reference the action by its `actionId` from a prior assistant message. `APPROVE` (the default) completes the action; `REJECT` records the rejection. Two kinds are actionable via the API: accepting a workflow suggestion (`APPROVE` applies the suggested workflow and immediately starts generating; the returned assistant message carries the workflow run in `generation`), and applying an assistant edit (an `APPLY_EDIT` action with `requiresApp` false, which applies the edit to the project). Actions with `requiresApp` set to true (plans, tools, and other app-only widgets) can only be completed in the web app: open the assistant's `projectUrl` instead. Asynchronous: the response contains the `messageId` of the resulting assistant message. Poll `GET /v1/assistant-messages/{messageId}` for its terminal state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assistant.with_raw_response.act_on_assistant_action("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ActOnAssistantActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.assistant.with_raw_response.act_on_assistant_action(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ActOnAssistantActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>assistant_id</code> | <code>str</code> | The assistant chat id (e.g. `vg_asst_...`). Every API project has one assistant chat; find it on `ProjectResponse.assistantId`. |
| <code>action_id</code> | <code>str</code> | The `actionId` of the action to act on, from a prior assistant message. |
| <code>body</code> | <code>[ActOnAssistantActionRequest](videogen/models/act_on_assistant_action_request.py) \| [ActOnAssistantActionRequestDict](videogen/models/act_on_assistant_action_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ActOnAssistantActionResponse](videogen/models/act_on_assistant_action_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ActOnAssistantActionResponse](videogen/models/act_on_assistant_action_response.py)</code> -- Assistant action accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_assistant(assistant_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetAssistantResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the assistant chat identified by `assistantId`, including every message in it (user and assistant turns) in chronological order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assistant.with_raw_response.get_assistant("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAssistantResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.assistant.with_raw_response.get_assistant("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAssistantResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>assistant_id</code> | <code>str</code> | The assistant chat id (e.g. `vg_asst_...`). Every API project has one assistant chat; find it on `ProjectResponse.assistantId`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[GetAssistantResponse](videogen/models/get_assistant_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetAssistantResponse](videogen/models/get_assistant_response.py)</code> -- The assistant chat and its messages.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_assistant_message(message_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AssistantMessage2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single assistant chat message by id. Poll after a POST that returned `messageId` until `status` is `succeeded`, `failed`, or `cancelled`. Also supported for `USER` messages (which reach terminal state as soon as they're accepted).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assistant.with_raw_response.get_assistant_message("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssistantMessage2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.assistant.with_raw_response.get_assistant_message("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AssistantMessage2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>message_id</code> | <code>str</code> | The assistant message id (e.g. `vg_mesg_...`) returned by an assistant POST. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[AssistantMessage2](videogen/models/unions/assistant_message2.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AssistantMessage2](videogen/models/unions/assistant_message2.py)</code> -- The assistant chat message.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_assistant_message(assistant_id: str, *, body: SendAssistantMessageRequest | SendAssistantMessageRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SendAssistantMessageResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a follow-up message to an existing assistant chat started with `POST /v1/assistants`. Asynchronous: the response contains the `messageId` of the assistant's pending reply. Poll `GET /v1/assistant-messages/{messageId}` until `status` is terminal, or subscribe to `assistant_message.*` webhooks.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assistant.with_raw_response.send_assistant_message("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SendAssistantMessageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.assistant.with_raw_response.send_assistant_message("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SendAssistantMessageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>assistant_id</code> | <code>str</code> | The assistant chat id (e.g. `vg_asst_...`). Every API project has one assistant chat; find it on `ProjectResponse.assistantId`. |
| <code>body</code> | <code>[SendAssistantMessageRequest](videogen/models/send_assistant_message_request.py) \| [SendAssistantMessageRequestDict](videogen/models/send_assistant_message_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[SendAssistantMessageResponse](videogen/models/send_assistant_message_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SendAssistantMessageResponse](videogen/models/send_assistant_message_response.py)</code> -- Assistant message accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_assistant_chat(*, body: StartAssistantChatRequest | StartAssistantChatRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartAssistantChatResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new project and sends the first message to the VideoGen AI assistant, exactly like typing into the assistant on a new project in the app. Asynchronous: the response contains the `messageId` of the assistant's pending reply (e.g. `vg_mesg_...`). Poll `GET /v1/assistant-messages/{messageId}` until `status` is `succeeded`, `failed`, or `cancelled`, or subscribe to `assistant_message.*` webhooks. Fetch the parent assistant with `GET /v1/assistants/{assistantId}` to list all messages in the chat.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.assistant.with_raw_response.start_assistant_chat()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartAssistantChatResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.assistant.with_raw_response.start_assistant_chat()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartAssistantChatResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[StartAssistantChatRequest](videogen/models/start_assistant_chat_request.py) \| [StartAssistantChatRequestDict](videogen/models/start_assistant_chat_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartAssistantChatResponse](videogen/models/start_assistant_chat_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartAssistantChatResponse](videogen/models/start_assistant_chat_response.py)</code> -- Assistant message accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Entities

> Source: [Entities](videogen/apis/entities.py)

<details>
<summary><code>def add_entity_reference(entity_id: str, *, body: AddEntityReferenceRequest | AddEntityReferenceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Entity, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Attach an image file as a reference for the entity. Upload the image first via `POST /v1/files/upload`. Returns the updated entity. Built-in entities (`isBuiltIn: true`) cannot have references added.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.add_entity_reference("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.add_entity_reference("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | The entity id (e.g. `vg_enti_...`). |
| <code>body</code> | <code>[AddEntityReferenceRequest](videogen/models/add_entity_reference_request.py) \| [AddEntityReferenceRequestDict](videogen/models/add_entity_reference_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[Entity](videogen/models/entity.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Entity](videogen/models/entity.py)</code> -- The updated entity

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def archive_entity(entity_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EntityArchiveResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archive an entity. Archived entities no longer appear in `GET /v1/entities` and can't be attached to new workflows. Built-in entities (`isBuiltIn: true`) cannot be archived.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.archive_entity("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EntityArchiveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.archive_entity("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EntityArchiveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | The entity id (e.g. `vg_enti_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[EntityArchiveResponse](videogen/models/entity_archive_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EntityArchiveResponse](videogen/models/entity_archive_response.py)</code> -- Archive acknowledged

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_entity(*, body: CreateEntityRequest | CreateEntityRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Entity, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new actor or visual style. Attach reference images with `POST /v1/entities/{entityId}/references`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.create_entity()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.create_entity()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateEntityRequest](videogen/models/create_entity_request.py) \| [CreateEntityRequestDict](videogen/models/create_entity_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[Entity](videogen/models/entity.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Entity](videogen/models/entity.py)</code> -- The created entity

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_entity(entity_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Entity, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a single entity by its id, including its reference images. Built-in catalog entities are included.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.get_entity("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.get_entity("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | The entity id (e.g. `vg_enti_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[Entity](videogen/models/entity.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Entity](videogen/models/entity.py)</code> -- Entity

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_entities(*, entity_type: V1EntitiesGetParametersEntityTypeOrStr | None = None, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListEntitiesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List built-in actors, products, visual styles, and slideshow themes, followed by the entities available to your team. Built-in entities have `isBuiltIn: true` and cannot be updated or archived. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.list_entities()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEntitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.list_entities()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEntitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_type</code> | <code>[V1EntitiesGetParametersEntityTypeOrStr](videogen/models/enums/v1_entities_get_parameters_entity_type.py) \| None</code> | When provided, returns only entities of this type. Omit to return all entities.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ListEntitiesResponse](videogen/models/list_entities_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListEntitiesResponse](videogen/models/list_entities_response.py)</code> -- Entity list

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_entity_reference(entity_id: str, *, body: RemoveEntityReferenceRequest | RemoveEntityReferenceRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Entity, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Detach a reference image from the entity. Returns the updated entity. Built-in entities (`isBuiltIn: true`) cannot have references removed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.remove_entity_reference("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.remove_entity_reference("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | The entity id (e.g. `vg_enti_...`). |
| <code>body</code> | <code>[RemoveEntityReferenceRequest](videogen/models/remove_entity_reference_request.py) \| [RemoveEntityReferenceRequestDict](videogen/models/remove_entity_reference_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[Entity](videogen/models/entity.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Entity](videogen/models/entity.py)</code> -- The updated entity

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_entity(entity_id: str, *, body: UpdateEntityRequest | UpdateEntityRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Entity, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update an entity's name or description. Provide at least one field. Built-in entities (`isBuiltIn: true`) cannot be updated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.entities.with_raw_response.update_entity("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.entities.with_raw_response.update_entity("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Entity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>entity_id</code> | <code>str</code> | The entity id (e.g. `vg_enti_...`). |
| <code>body</code> | <code>[UpdateEntityRequest](videogen/models/update_entity_request.py) \| [UpdateEntityRequestDict](videogen/models/update_entity_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[Entity](videogen/models/entity.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Entity](videogen/models/entity.py)</code> -- The updated entity

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Files

> Source: [Files](videogen/apis/files.py)

<details>
<summary><code>def archive_file(file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileInfo, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Archive a file by setting its archived timestamp. Archived files are excluded from list results. Returns the updated file object.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.archive_file("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.archive_file("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file_id</code> | <code>str</code> | The file id (e.g. `vg_file_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[FileInfo](videogen/models/file_info.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileInfo](videogen/models/file_info.py)</code> -- Archived file

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_file_upload(*, body: CreateFileUploadRequest | CreateFileUploadRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileUploadResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new file and receive a pre-signed upload URL. PUT the file bytes to the returned URL, then poll `GET /v1/files/{fileId}` until the file is ready.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.create_file_upload()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileUploadResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.create_file_upload()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileUploadResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateFileUploadRequest](videogen/models/create_file_upload_request.py) \| [CreateFileUploadRequestDict](videogen/models/create_file_upload_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[FileUploadResponse](videogen/models/file_upload_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileUploadResponse](videogen/models/file_upload_response.py)</code> -- Upload instructions

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_public_preview(file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileInfo, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disable public preview for a file. Removes the permanent public URL copy and revokes unauthenticated embed streaming access. Authenticated signed URLs remain functional. Returns the updated file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.disable_public_preview("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.disable_public_preview("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file_id</code> | <code>str</code> | The file id (e.g. `vg_file_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[FileInfo](videogen/models/file_info.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileInfo](videogen/models/file_info.py)</code> -- File with public preview disabled

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_public_preview(file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileInfo, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable public preview for a file. Works for any file type. Copies the file to a permanent public URL (`staticPublicPreviewSource`) and, for video and audio, registers a public embed playback id (`publicPlaybackId`) for use with `@videogen/player`. If streaming playback is still processing, the endpoint polls briefly and background processing finishes creating the embed playback id. Returns the updated file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.enable_public_preview("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.enable_public_preview("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file_id</code> | <code>str</code> | The file id (e.g. `vg_file_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[FileInfo](videogen/models/file_info.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileInfo](videogen/models/file_info.py)</code> -- File with public preview enabled

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_file(file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileInfo, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve metadata for a single file by its id.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.get_file("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.get_file("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file_id</code> | <code>str</code> | The file id (e.g. `vg_file_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[FileInfo](videogen/models/file_info.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileInfo](videogen/models/file_info.py)</code> -- File metadata

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_files(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, include_export_files: bool | None = False, include_project_files: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetFilesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List files accessible to your team. By default this returns standalone files (direct tool-call outputs and uploads) and omits two categories: export files (the raw output files of your exports) and project files (the generative files created within a project, e.g. each AI image and text-to-speech file in a script-to-video workflow output). Set `includeExportFiles` and/or `includeProjectFiles` to true to include them. Use `selfOnly=true` to restrict results to files created by the calling API key's user. Files are returned most recently updated first. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.get_files()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.get_files()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>self_only</code> | <code>bool \| None</code> | When true, returns only items created by the API key's owner. When false (default), returns all items accessible to the team.<br>**Default**: <code>False</code> |
| <code>include_export_files</code> | <code>bool \| None</code> | When true, includes export files: the raw output files of your exports (the rendered MP4 you download from an export). When false (default), they are omitted.<br>**Default**: <code>False</code> |
| <code>include_project_files</code> | <code>bool \| None</code> | When true, includes project files: the generative files created within a project (e.g. each AI image and text-to-speech file produced inside a script-to-video workflow output). When false (default), they are omitted.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[GetFilesResponse](videogen/models/get_files_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetFilesResponse](videogen/models/get_files_response.py)</code> -- File list

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def hydrate_file(file_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileInfo, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate fresh signed URLs for all available renditions of a file. Call this when source URLs are missing or expired. Returns the full file object with populated `downloadSource`, `thumbnailSource`, and `previewSource` (and the convenience root-level `downloadUrl` / `thumbnailUrl`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.hydrate_file("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.hydrate_file("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>file_id</code> | <code>str</code> | The file id (e.g. `vg_file_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[FileInfo](videogen/models/file_info.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FileInfo](videogen/models/file_info.py)</code> -- File with hydrated sources

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_files(*, body: SearchFilesRequest | SearchFilesRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchFilesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Semantic vector search over your files. Embeds the query text and returns the closest matching files ranked by cosine similarity. Only files with indexed descriptions are searchable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.files.with_raw_response.search_files()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.files.with_raw_response.search_files()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchFilesRequest](videogen/models/search_files_request.py) \| [SearchFilesRequestDict](videogen/models/search_files_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[SearchFilesResponse](videogen/models/search_files_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchFilesResponse](videogen/models/search_files_response.py)</code> -- Search results ordered by descending similarity

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Projects

> Source: [Projects](videogen/apis/projects.py)

<details>
<summary><code>def create_timeline_interchange(project_id: str, *, body: CreateTimelineInterchangeRequest | CreateTimelineInterchangeRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTimelineInterchangeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Starts a timeline interchange job that converts a project into an editor interchange document (Final Cut Pro FCPXML, Adobe Premiere Pro XML, OpenTimelineIO, or an SRT caption sidecar). Returns immediately with an interchange job id; the file becomes available when the job completes. Unlike `POST /v1/projects/{projectId}/export` (which renders a flattened MP4), this preserves the project as an editable timeline of separate clips, tracks, and captions so you can keep editing it in a desktop video editor. Choose `mediaDelivery` to control how the document references media: `REMOTE_URLS` produces a single document that links to signed media URLs, while `BUNDLE` produces a zip containing the document plus every referenced media file for durable offline relinking.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.create_timeline_interchange("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTimelineInterchangeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.create_timeline_interchange("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTimelineInterchangeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>body</code> | <code>[CreateTimelineInterchangeRequest](videogen/models/create_timeline_interchange_request.py) \| [CreateTimelineInterchangeRequestDict](videogen/models/create_timeline_interchange_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[CreateTimelineInterchangeResponse](videogen/models/create_timeline_interchange_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTimelineInterchangeResponse](videogen/models/create_timeline_interchange_response.py)</code> -- Timeline interchange accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def export_project(project_id: str, *, body: ExportProjectRequest | ExportProjectRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ExportProjectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Starts an export of a project to MP4. Returns immediately with an export id; the file becomes available when the export task completes. Exporting requires a paid plan in the app, but the API lets you export for free with a VideoGen watermark and a short 'Made with VideoGen' end screen appended to the video. A Pro plan lets you remove both by setting `watermarkMode` and `endScreenMode` to `NONE`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.export_project("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ExportProjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.export_project("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ExportProjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>body</code> | <code>[ExportProjectRequest](videogen/models/export_project_request.py) \| [ExportProjectRequestDict](videogen/models/export_project_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ExportProjectResponse](videogen/models/export_project_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ExportProjectResponse](videogen/models/export_project_response.py)</code> -- Export accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_project(project_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProjectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a simplified view of a project including its title, aspect ratio, status, and URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.get_project("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.get_project("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ProjectResponse](videogen/models/project_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProjectResponse](videogen/models/project_response.py)</code> -- Project metadata.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_project_export(project_id: str, export_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProjectExport, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current status of a project export started via `POST /v1/projects/{projectId}/export`, and — once `status` is `succeeded` — the signed download/thumbnail URLs and the hydrated export `file`. Poll this endpoint until `status` is `succeeded`, `failed`, or `cancelled`. The signed URLs are private and valid for 7 days; this endpoint automatically re-signs them when they are within an hour of expiring, so a caller always receives a URL valid long enough to use. Every endpoint that returns hydrated files auto-rehydrates this way — only the file endpoints (`GET /v1/files/{fileId}` and `POST /v1/files/{fileId}/hydrate`) are the explicit, on-demand hydration paths. Use `exportFileId` with `POST /v1/files/{fileId}/hydrate` if you need to re-sign the export file directly later.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.get_project_export("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProjectExport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.get_project_export("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProjectExport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>export_id</code> | <code>str</code> | The export id (e.g. `vg_expo_...`) returned by `POST /v1/projects/{projectId}/export`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ProjectExport](videogen/models/project_export.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProjectExport](videogen/models/project_export.py)</code> -- Export status.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_timeline_interchange(interchange_job_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TimelineInterchange, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current status of a timeline interchange job started via `POST /v1/projects/{projectId}/timeline-interchange`, and, once `status` is `succeeded`, the signed download URL and the hydrated interchange `file`. Poll this endpoint until `status` is `succeeded`, `failed`, or `cancelled`. The signed URL is private and valid for 7 days; this endpoint automatically re-signs it when it is within an hour of expiring. Use `interchangeFileId` with `POST /v1/files/{fileId}/hydrate` if you need to re-sign the file directly later.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.get_timeline_interchange("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TimelineInterchange
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.get_timeline_interchange("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TimelineInterchange
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>interchange_job_id</code> | <code>str</code> | The timeline interchange job id (e.g. `vg_inte_...`) returned by `POST /v1/projects/{projectId}/timeline-interchange`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[TimelineInterchange](videogen/models/timeline_interchange.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TimelineInterchange](videogen/models/timeline_interchange.py)</code> -- Timeline interchange status.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_project_exports(project_id: str, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectExportsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a project's exports, newest first, as fully hydrated `ProjectExport` objects (status, signed download/thumbnail URLs, and the embedded `file`). Signed URLs are re-signed when within an hour of expiring, so they are always valid long enough to use. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.list_project_exports("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectExportsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.list_project_exports("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectExportsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ListProjectExportsResponse](videogen/models/list_project_exports_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectExportsResponse](videogen/models/list_project_exports_response.py)</code> -- Project exports.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_project_remix_actions(project_id: str, *, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListRemixActionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns remix actions applied to a project (via `POST /v1/projects/{projectId}/remix` or as a post-workflow step), most recent first, with each action's status and progress. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.list_project_remix_actions("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRemixActionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.list_project_remix_actions("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListRemixActionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ListRemixActionsResponse](videogen/models/list_remix_actions_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListRemixActionsResponse](videogen/models/list_remix_actions_response.py)</code> -- Remix actions for the project.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_projects(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, include_ui_projects: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListProjectsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns projects, most recently updated first. By default only API-created projects are included; pass `includeUiProjects=true` to also include dashboard-created projects. Use `selfOnly=true` to restrict results to the calling API key's user; otherwise all matching projects for the team are returned. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.list_projects()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.list_projects()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListProjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>self_only</code> | <code>bool \| None</code> | When true, returns only items created by the API key's owner. When false (default), returns all items accessible to the team.<br>**Default**: <code>False</code> |
| <code>include_ui_projects</code> | <code>bool \| None</code> | When true, includes dashboard-created projects in addition to API-created projects. When false (default), returns only API-created projects.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ListProjectsResponse](videogen/models/list_projects_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListProjectsResponse](videogen/models/list_projects_response.py)</code> -- Paginated list of projects.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remix_project(project_id: str, *, body: RemixProjectRequest | RemixProjectRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RemixProjectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Applies an ordered list of edits (background music, logo overlay, caption visibility/style) to a project. Each action runs asynchronously as its own remix action; the response returns one remix action id per action in order. Set `saveAsNewProject` to apply the edits to a copy and leave the original untouched. Poll `GET /v1/projects/{projectId}/remix-actions` for status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.projects.with_raw_response.remix_project("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RemixProjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.projects.with_raw_response.remix_project("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RemixProjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>project_id</code> | <code>str</code> | The project id (e.g. `vg_proj_...`). |
| <code>body</code> | <code>[RemixProjectRequest](videogen/models/remix_project_request.py) \| [RemixProjectRequestDict](videogen/models/remix_project_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[RemixProjectResponse](videogen/models/remix_project_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RemixProjectResponse](videogen/models/remix_project_response.py)</code> -- Remix actions accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Resources

> Source: [Resources](videogen/apis/resources.py)

<details>
<summary><code>def list_languages(*, query: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LanguageListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List the languages a project can be translated into. Pass a `languageCode` from the response to the `TRANSLATE_PROJECT` remix action. Returns the full catalogue in a single response (not paginated). Pass `query` to filter by language code or English name.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.resources.with_raw_response.list_languages()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LanguageListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.resources.with_raw_response.list_languages()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LanguageListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query</code> | <code>str \| None</code> | Optional case-insensitive substring filter across each item's searchable text fields. Omit to return the unfiltered catalogue.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[LanguageListResponse](videogen/models/language_list_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LanguageListResponse](videogen/models/language_list_response.py)</code> -- List of supported languages. Pass a `languageCode` to a `TRANSLATE_PROJECT` remix action.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_tts_voices(*, limit: int | None = 50, cursor: str | None = None, include_deprecated_voices: bool | None = False, query: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TtsVoiceListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List available text-to-speech voices. Pass a `voiceId` or `displayName` from the response to the text-to-speech endpoint. Cursor-paginated; see the [Pagination](/pagination) guide. Pass `query` to filter by voice id, display name, language, accent, or description.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.resources.with_raw_response.list_tts_voices()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TtsVoiceListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.resources.with_raw_response.list_tts_voices()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TtsVoiceListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>include_deprecated_voices</code> | <code>bool \| None</code> | When true, includes voices that are deprecated but still callable. Defaults to false.<br>**Default**: <code>False</code> |
| <code>query</code> | <code>str \| None</code> | Optional case-insensitive substring filter across each item's searchable text fields. Omit to return the unfiltered catalogue.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[TtsVoiceListResponse](videogen/models/tts_voice_list_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TtsVoiceListResponse](videogen/models/tts_voice_list_response.py)</code> -- List of TTS voices. Pass a `voiceId` or `displayName` to `POST /v1/tools/text-to-speech`.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Text

> Source: [Text](videogen/apis/text.py)

<details>
<summary><code>def generate_text(*, body: GenerateTextRequest | GenerateTextRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateTextResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate text from a prompt using a general-purpose language model. Choose a quality tier with `quality` (`LOW`, `STANDARD`, `HIGH`, or `MAX`). Synchronous: the response includes the generated text. Useful for drafting scripts, titles, descriptions, and other short copy before generating a video.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.text.with_raw_response.generate_text()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateTextResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.text.with_raw_response.generate_text()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateTextResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateTextRequest](videogen/models/generate_text_request.py) \| [GenerateTextRequestDict](videogen/models/generate_text_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[GenerateTextResponse](videogen/models/generate_text_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateTextResponse](videogen/models/generate_text_response.py)</code> -- Generated text.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Tools

> Source: [Tools](videogen/apis/tools.py)

<details>
<summary><code>def cancel_tool_execution(tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Request cancellation of a running tool execution. The execution transitions to `cancelled` if it has not already completed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.cancel_tool_execution("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.cancel_tool_execution("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>tool_execution_id</code> | <code>str</code> | The tool execution id returned when the tool was started. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Cancellation request accepted

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_avatar(*, body: GenerateAvatarRequest | GenerateAvatarRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate a talking-head avatar video by pairing an ACTOR entity with an audio file, typically from a prior text-to-speech result.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.generate_avatar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.generate_avatar()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateAvatarRequest](videogen/models/generate_avatar_request.py) \| [GenerateAvatarRequestDict](videogen/models/generate_avatar_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_image(*, body: GenerateImageRequest | GenerateImageRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate an image from a text prompt, optionally guided by reference images and actor, product, or visual-style entity ids. When reference images are provided, the prompt describes the desired transformation. VideoGen automatically routes each request to the most effective state-of-the-art image model for your prompt, reference images, entities, and quality tier, so you don't pick a model.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.generate_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.generate_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateImageRequest](videogen/models/generate_image_request.py) \| [GenerateImageRequestDict](videogen/models/generate_image_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_motion_graphic(*, body: GenerateMotionGraphicRequest | GenerateMotionGraphicRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate an animated motion graphic video from a text prompt. This is an experimental, fully agentic alternative to a video workflow: VideoGen plans the animation, optionally generates or fetches supporting media, and renders a self-contained animated clip. It is especially well suited to precise text animations (e.g. a typing effect, animated captions, kinetic typography, lower thirds) that are hard to express with stock or generated footage. Optionally pass uploaded `fileIds` for reference media and `entityIds` for actors, products, or visual styles the animation should use. This endpoint returns one standalone video. For longer, narrated, multi-scene videos, use a video workflow such as [Script to video](/workflows) (`POST /v1/workflows/script-to-video`) instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.generate_motion_graphic()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.generate_motion_graphic()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateMotionGraphicRequest](videogen/models/generate_motion_graphic_request.py) \| [GenerateMotionGraphicRequestDict](videogen/models/generate_motion_graphic_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_music(*, body: GenerateMusicRequest | GenerateMusicRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate an instrumental music track from a text description. The returned track is approximately 30 seconds long. VideoGen automatically routes each request to the most effective state-of-the-art music model for your prompt, so you don't pick a model.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.generate_music()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.generate_music()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateMusicRequest](videogen/models/generate_music_request.py) \| [GenerateMusicRequestDict](videogen/models/generate_music_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_sound_effect(*, body: GenerateSoundEffectRequest | GenerateSoundEffectRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate a sound effect from a text description. Optionally control the duration and prompt influence. VideoGen automatically routes each request to the most effective state-of-the-art sound effect model for your prompt and settings, so you don't pick a model.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.generate_sound_effect()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.generate_sound_effect()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateSoundEffectRequest](videogen/models/generate_sound_effect_request.py) \| [GenerateSoundEffectRequestDict](videogen/models/generate_sound_effect_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_video_clip(*, body: GenerateVideoClipRequest | GenerateVideoClipRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Generate a single short video clip (up to 30 seconds) from a text prompt, optionally guided by an opening-frame still, reference images, videos, and audio. At least one of `prompt`, `startFrameFileId`, `imageFileIds`, `videoFileIds`, `audioFileIds`, or `spokenDialogue` must be provided. VideoGen automatically routes each request to the most effective state-of-the-art video model for your inputs and settings, so you don't pick a model. This endpoint returns one standalone clip. For longer, higher-quality, professionally edited videos with narration, captions, music, and multiple scenes, use a video workflow such as [Script to video](/workflows) (`POST /v1/workflows/script-to-video`) instead.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.generate_video_clip()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.generate_video_clip()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateVideoClipRequest](videogen/models/generate_video_clip_request.py) \| [GenerateVideoClipRequestDict](videogen/models/generate_video_clip_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_tool_execution_info(tool_execution_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ExecutedTool, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the current status and result of a tool execution. Poll this endpoint until `status` is `succeeded`, `failed`, or `cancelled`. Each succeeded result carries signed `downloadUrl`/`thumbnailUrl` (with matching `*ExpiresAt` timestamps) alongside the full hydrated `file`. The signed URLs are private and valid for 7 days; this single-execution endpoint automatically re-signs them when they are within an hour of expiring, so a caller always receives a URL valid long enough to use. Results remain retrievable indefinitely, including executions older than 7 days. Note that list endpoints (e.g. `GET /v1/tools/executions`) do not re-sign URLs: they return the last-signed URL, which may already be expired (check `downloadUrlExpiresAt`). To refresh a URL, GET the individual execution here, or hydrate the file directly via `GET /v1/files/{fileId}` / `POST /v1/files/{fileId}/hydrate`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.get_tool_execution_info("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ExecutedTool
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.get_tool_execution_info("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ExecutedTool
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>tool_execution_id</code> | <code>str</code> | The tool execution id returned when the tool was started. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ExecutedTool](videogen/models/executed_tool.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ExecutedTool](videogen/models/executed_tool.py)</code> -- Current execution state

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def image3d_effect(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Turn a still image into a short video clip with a 3D parallax motion effect, simulating camera movement through the scene.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.image3d_effect()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.image3d_effect()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ImageAssetRequest](videogen/models/image_asset_request.py) \| [ImageAssetRequestDict](videogen/models/image_asset_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_tool_executions(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ToolExecutionListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List tool executions started via the API, most recently created first. Use `selfOnly=true` to restrict results to the calling API key's user; otherwise all executions for the team are returned. Cursor-paginated; see the [Pagination](/pagination) guide. Executions remain listable indefinitely (including those older than 7 days). For efficiency this list does not re-sign result download URLs, so `downloadUrl`/`thumbnailUrl` reflect the last time they were signed and may be expired (always check `downloadUrlExpiresAt`). To obtain a fresh signed URL, GET the individual execution (`GET /v1/tools/executions/{toolExecutionId}`) or hydrate the file (`GET /v1/files/{fileId}` / `POST /v1/files/{fileId}/hydrate`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.list_tool_executions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ToolExecutionListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.list_tool_executions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ToolExecutionListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>self_only</code> | <code>bool \| None</code> | When true, returns only items created by the API key's owner. When false (default), returns all items accessible to the team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[ToolExecutionListResponse](videogen/models/tool_execution_list_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ToolExecutionListResponse](videogen/models/tool_execution_list_response.py)</code> -- Paginated list of tool executions.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_image_background(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the background from an image, returning a transparent-background PNG of the foreground subject.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.remove_image_background()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.remove_image_background()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ImageAssetRequest](videogen/models/image_asset_request.py) \| [ImageAssetRequestDict](videogen/models/image_asset_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_video_background(*, body: VideoAssetRequest | VideoAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove the background from a video, producing a transparent-background video of the foreground subject.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.remove_video_background()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.remove_video_background()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[VideoAssetRequest](videogen/models/video_asset_request.py) \| [VideoAssetRequestDict](videogen/models/video_asset_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def text_to_speech(*, body: TextToSpeechRequest | TextToSpeechRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert text into a spoken audio file. Only voices with `supportsDirectToolExecution` set to true can be used. Optionally choose a voice, language, speed, and pronunciation overrides.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.text_to_speech()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.text_to_speech()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[TextToSpeechRequest](videogen/models/text_to_speech_request.py) \| [TextToSpeechRequestDict](videogen/models/text_to_speech_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upscale_image(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Increase the resolution of an image while preserving detail and sharpness.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.upscale_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.upscale_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ImageAssetRequest](videogen/models/image_asset_request.py) \| [ImageAssetRequestDict](videogen/models/image_asset_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upscale_video(*, body: VideoAssetRequest | VideoAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Increase the resolution of a video while preserving detail and sharpness.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.upscale_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.upscale_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[VideoAssetRequest](videogen/models/video_asset_request.py) \| [VideoAssetRequestDict](videogen/models/video_asset_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def vectorize_image(*, body: ImageAssetRequest | ImageAssetRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartToolExecutionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convert any raster image into a scalable vector graphic (SVG). The output traces the shapes and colors of the input image.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.tools.with_raw_response.vectorize_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.tools.with_raw_response.vectorize_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartToolExecutionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ImageAssetRequest](videogen/models/image_asset_request.py) \| [ImageAssetRequestDict](videogen/models/image_asset_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartToolExecutionResponse](videogen/models/start_tool_execution_response.py)</code> -- Execution accepted; poll until complete.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Webhooks

> Source: [Webhooks](videogen/apis/webhooks.py)

<details>
<summary><code>def create_webhook_endpoint(*, body: CreateWebhookEndpointRequest | CreateWebhookEndpointRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WebhookEndpoint, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Register a new webhook endpoint to receive `tool_execution.*`, `workflow_run.*`, and `file.*` events. The signing secret is only returned in this response. Store it securely.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhooks.with_raw_response.create_webhook_endpoint()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WebhookEndpoint
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhooks.with_raw_response.create_webhook_endpoint()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WebhookEndpoint
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateWebhookEndpointRequest](videogen/models/create_webhook_endpoint_request.py) \| [CreateWebhookEndpointRequestDict](videogen/models/create_webhook_endpoint_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[WebhookEndpoint](videogen/models/webhook_endpoint.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WebhookEndpoint](videogen/models/webhook_endpoint.py)</code> -- Created; `signingSecret` is only returned in this response.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_webhook_endpoint(endpoint_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a webhook endpoint. It will stop receiving events immediately.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhooks.with_raw_response.delete_webhook_endpoint("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhooks.with_raw_response.delete_webhook_endpoint("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>endpoint_id</code> | <code>str</code> | The webhook endpoint id (e.g. `ep_...`) returned by `POST /v1/webhooks/endpoints`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;Any, [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Removed

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_webhook_endpoints(*, limit: int | None = 50, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WebhookEndpointListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List configured webhook endpoints for your account. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhooks.with_raw_response.list_webhook_endpoints()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WebhookEndpointListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhooks.with_raw_response.list_webhook_endpoints()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WebhookEndpointListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[WebhookEndpointListResponse](videogen/models/webhook_endpoint_list_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WebhookEndpointListResponse](videogen/models/webhook_endpoint_list_response.py)</code> -- Configured endpoints

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Workflows

> Source: [Workflows](videogen/apis/workflows.py)

<details>
<summary><code>def cancel_workflow_run(workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartWorkflowRunResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.cancel_workflow_run("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.cancel_workflow_run("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>workflow_run_id</code> | <code>str</code> | The workflow run id returned when the workflow was started. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py)</code> -- Cancellation request accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_workflow_run(workflow_run_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WorkflowRun, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.get_workflow_run("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WorkflowRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.get_workflow_run("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WorkflowRun
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>workflow_run_id</code> | <code>str</code> | The workflow run id returned when the workflow was started. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[WorkflowRun](videogen/models/workflow_run.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WorkflowRun](videogen/models/workflow_run.py)</code> -- Current workflow run state.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_workflow_runs(*, limit: int | None = 50, cursor: str | None = None, self_only: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WorkflowRunListResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List workflow runs started via the API, most recently created first. Use `selfOnly=true` to restrict results to the calling API key's user; otherwise all runs for the team are returned. Cursor-paginated; see the [Pagination](/pagination) guide.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.list_workflow_runs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WorkflowRunListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.list_workflow_runs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WorkflowRunListResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | Maximum number of items to return in the page. Defaults to 50; capped at 200. See [Pagination](/pagination).<br>**Default**: <code>50</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque pagination cursor returned as `nextCursor` by the previous page. Omit on the first request. Cursors are tied to the endpoint that produced them and must be passed unmodified. See [Pagination](/pagination).<br>**Default**: <code>None</code> |
| <code>self_only</code> | <code>bool \| None</code> | When true, returns only items created by the API key's owner. When false (default), returns all items accessible to the team.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[WorkflowRunListResponse](videogen/models/workflow_run_list_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WorkflowRunListResponse](videogen/models/workflow_run_list_response.py)</code> -- Paginated list of workflow runs.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def prompt_to_video_clip(*, body: PromptToVideoClipRequest | PromptToVideoClipRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartWorkflowRunResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a project from a text prompt and generates one short AI video clip (up to 30 seconds). VideoGen first generates an opening frame from the prompt (optionally guided by reference images), then animates that frame into a video. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion. For a standalone clip without an editable project, use `POST /v1/tools/generate-video-clip` instead. For longer narrated multi-scene videos, use `POST /v1/workflows/script-to-video`. The generated clip is clamped to the selected quality's supported range.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.prompt_to_video_clip()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.prompt_to_video_clip()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PromptToVideoClipRequest](videogen/models/prompt_to_video_clip_request.py) \| [PromptToVideoClipRequestDict](videogen/models/prompt_to_video_clip_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py)</code> -- Workflow run accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def script_to_video(*, body: ScriptToVideoRequest | ScriptToVideoRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartWorkflowRunResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a project and generates a narrated video from a prompt or script. Returns immediately with a workflow run id; poll or subscribe to webhooks for completion.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.script_to_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.script_to_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ScriptToVideoRequest](videogen/models/script_to_video_request.py) \| [ScriptToVideoRequestDict](videogen/models/script_to_video_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py)</code> -- Workflow run accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def slideshow_to_video(*, body: SlideshowToVideoRequest | SlideshowToVideoRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartWorkflowRunResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a project from an uploaded PDF or PowerPoint file and generates an AI-narrated video walking through each slide. Upload the file via `POST /v1/files/upload` first.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.slideshow_to_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.slideshow_to_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SlideshowToVideoRequest](videogen/models/slideshow_to_video_request.py) \| [SlideshowToVideoRequestDict](videogen/models/slideshow_to_video_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py)</code> -- Workflow run accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def voiceover_to_video(*, body: VoiceoverToVideoRequest | VoiceoverToVideoRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartWorkflowRunResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a project from an uploaded voiceover file and generates a video with matching b-roll. Upload the voiceover via the files API first.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.workflows.with_raw_response.voiceover_to_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.workflows.with_raw_response.voiceover_to_video()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartWorkflowRunResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[VoiceoverToVideoRequest](videogen/models/voiceover_to_video_request.py) \| [VoiceoverToVideoRequestDict](videogen/models/voiceover_to_video_request.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](videogen/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](videogen/core/results.py)&#91;[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py), [RawError](videogen/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartWorkflowRunResponse](videogen/models/start_workflow_run_response.py)</code> -- Workflow run accepted.

**On `Failure`**: `error` is <code>[RawError](videogen/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

