from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class TranscriptWord(SdkBaseModel):
    """A single timed word of a transcript."""

    start_seconds: float = Field(alias="startSeconds")
    """Start time of the word in seconds from the beginning of the audio."""

    end_seconds: float = Field(alias="endSeconds")
    """End time of the word in seconds from the beginning of the audio. Must be greater than ``startSeconds``."""

    word: str
    """The spoken word, used verbatim for narration timing and captions."""


class TranscriptWordDict(TypedDict):
    start_seconds: float
    end_seconds: float
    word: str
