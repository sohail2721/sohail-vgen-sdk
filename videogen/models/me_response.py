from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class MeResponse(SdkBaseModel):
    api_key_id: str = Field(alias="apiKeyId")
    """The id of the API key used to authenticate this request."""

    api_key_nickname: str = Field(alias="apiKeyNickname")
    """The nickname given to the API key when it was created."""

    email: str
    """The email address of the account the API key belongs to."""

    display_name: str | None = Field(alias="displayName")
    """The display name of the account the API key belongs to. ``null`` if the account has not set one."""

    team_id: str = Field(alias="teamId")
    """The id of the team the API key belongs to."""


class MeResponseDict(TypedDict):
    api_key_id: str
    api_key_nickname: str
    email: str
    display_name: str | None
    team_id: str
