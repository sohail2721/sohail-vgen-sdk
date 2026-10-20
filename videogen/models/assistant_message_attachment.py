from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class AssistantMessageAttachment(SdkBaseModel):
    """A file linked to an assistant chat message."""

    file_id: OptionalNullable[str] = Field(default=UNSET, alias="fileId")
    """File id (e.g. ``vg_file_...``) when the attachment is a storage file. ``null`` for attachments that are not
    resolvable storage files."""

    display_name: str = Field(alias="displayName")
    """Human-readable name of the attachment."""


class AssistantMessageAttachmentDict(TypedDict):
    file_id: NotRequired[str | None]
    display_name: str
