from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .pronunciation_replacement import PronunciationReplacement, PronunciationReplacementDict


class TextToSpeechRequest(SdkBaseModel):
    tts_text: str = Field(alias="ttsText")
    voice_id: str = Field(alias="voiceId")
    """Catalog ``displayName`` (e.g. ``Matilda``) or voice id from ``GET /v1/resources/tts-voices`` (e.g.
    ``vg_voic_...``). Only voices with ``supportsDirectToolExecution`` set to true are accepted."""

    speech_language_code: OptionalNullable[str] = Field(default=UNSET, alias="speechLanguageCode")
    """ISO-639-1 language hint for pronunciation (e.g. ``en``, ``es``, ``zh``)."""

    pronunciation_replacements: Optional[list[PronunciationReplacement]] = Field(
        default=UNSET, alias="pronunciationReplacements"
    )
    auto_expand_pronunciation_replacements: Optional[bool] = Field(
        default=UNSET, alias="autoExpandPronunciationReplacements"
    )
    """When true, automatically expands numbers, symbols, acronyms, and other non-word tokens into their spoken forms
    before synthesis so the voice pronounces them correctly (e.g. ``$100`` → ``one hundred dollars``, ``NASA`` →
    ``nasa``, ``3rd`` → ``third``). Defaults to false when omitted."""

    voice_speed: Optional[float] = Field(default=UNSET, alias="voiceSpeed")
    """Speech rate multiplier, between 0.5 (half speed) and 2 (double speed). Defaults to the voice's default speed."""

    num_results: int = Field(default=1, alias="numResults")
    """Number of output results to generate. Defaults to 1."""

    is_output_temporary: bool = Field(default=False, alias="isOutputTemporary")
    """When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after
    which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding
    will be generated), so they will not appear in search results. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, generated files are hidden from the VideoGen Media page by default. They remain accessible through the
    API. Defaults to false."""


class TextToSpeechRequestDict(TypedDict):
    tts_text: str
    voice_id: str
    speech_language_code: NotRequired[str | None]
    pronunciation_replacements: NotRequired[list[PronunciationReplacementDict]]
    auto_expand_pronunciation_replacements: NotRequired[bool]
    voice_speed: NotRequired[float]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
