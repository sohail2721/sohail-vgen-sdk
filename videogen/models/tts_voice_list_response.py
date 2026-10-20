from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .tts_voice import TtsVoice, TtsVoiceDict


class TtsVoiceListResponse(SdkBaseModel):
    tts_voices: list[TtsVoice] = Field(alias="ttsVoices")
    has_more: bool = Field(alias="hasMore")
    """When true, there are more voices available. Pass ``nextCursor`` as the ``cursor`` query param to fetch the next
    page."""

    next_cursor: str | None = Field(alias="nextCursor")
    """Opaque cursor to fetch the next page. ``null`` when ``hasMore`` is false."""


class TtsVoiceListResponseDict(TypedDict):
    tts_voices: list[TtsVoiceDict]
    has_more: bool
    next_cursor: str | None
