from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class WebhookEventName(str, Enum):
    """All webhook event types. Use when creating or listing webhook endpoints."""

    TOOL_EXECUTION_SUCCEEDED = "tool_execution.succeeded"
    TOOL_EXECUTION_FAILED = "tool_execution.failed"
    TOOL_EXECUTION_CANCELLED = "tool_execution.cancelled"
    WORKFLOW_RUN_SUCCEEDED = "workflow_run.succeeded"
    WORKFLOW_RUN_FAILED = "workflow_run.failed"
    WORKFLOW_RUN_CANCELLED = "workflow_run.cancelled"
    PROJECT_EXPORT_SUCCEEDED = "project_export.succeeded"
    PROJECT_EXPORT_FAILED = "project_export.failed"
    PROJECT_EXPORT_CANCELLED = "project_export.cancelled"
    ASSISTANT_MESSAGE_SUCCEEDED = "assistant_message.succeeded"
    ASSISTANT_MESSAGE_FAILED = "assistant_message.failed"
    ASSISTANT_MESSAGE_CANCELLED = "assistant_message.cancelled"
    FILE_UPLOAD_COMPLETED = "file.upload.completed"
    FILE_UPLOAD_FAILED = "file.upload.failed"
    FILE_PLAYBACK_READY = "file.playback_ready"
    FILE_DOWNLOAD_READY = "file.download_ready"
    FILE_ANALYSIS_COMPLETED = "file.analysis_completed"
    FILE_ANALYSIS_FAILED = "file.analysis_failed"

    __str__ = str.__str__


WebhookEventNameOrStr: TypeAlias = Annotated[WebhookEventName | str, open_enum_validator(WebhookEventName)]
