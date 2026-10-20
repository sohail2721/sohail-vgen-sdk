from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.export_delivery_destination_type import ExportDeliveryDestinationTypeOrStr


class ExportDeliveryDestination(SdkBaseModel):
    integration_connection_id: str = Field(alias="integrationConnectionId")
    """Id of the connected integration that will receive this export."""

    type_: ExportDeliveryDestinationTypeOrStr = Field(alias="type")
    """Where to deliver the export within the connected integration."""

    slack_channel_id: OptionalNullable[str] = Field(default=UNSET, alias="slackChannelId")
    """Target channel id. Required when ``type`` is ``SLACK_CHANNEL``."""

    google_drive_folder_id: OptionalNullable[str] = Field(default=UNSET, alias="googleDriveFolderId")
    """Target folder id. Required when ``type`` is ``GOOGLE_DRIVE_FOLDER``."""


class ExportDeliveryDestinationDict(TypedDict):
    integration_connection_id: str
    type_: ExportDeliveryDestinationTypeOrStr
    slack_channel_id: NotRequired[str | None]
    google_drive_folder_id: NotRequired[str | None]
