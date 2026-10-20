from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .transcript_word import TranscriptWord, TranscriptWordDict


class Transcript(SdkBaseModel):
    """A transcript of an audio file, as timed words in order."""

    language_code: OptionalNullable[str] = Field(default=UNSET, alias="languageCode")
    """Optional BCP-47 language code of the spoken audio (e.g. ``en``, ``es``). Used to tag the transcript's language;
    omit if unknown."""

    words: list[TranscriptWord]
    """The transcript words, sorted by ``startSeconds`` and non-overlapping. Must contain at least one word."""


class TranscriptDict(TypedDict):
    language_code: NotRequired[str | None]
    words: list[TranscriptWordDict]
