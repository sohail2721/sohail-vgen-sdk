from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .enums.tts_voice_display_gender import TtsVoiceDisplayGenderOrStr


class TtsVoice(SdkBaseModel):
    """A text-to-speech voice."""

    voice_id: str = Field(alias="voiceId")
    """Voice id (e.g. ``vg_voic_...``). Pass this or ``displayName`` as ``voiceId`` to ``POST
    /v1/tools/text-to-speech``."""

    language_code: str = Field(alias="languageCode")
    """Locale tag for the voice (e.g. ``en-US``, ``es-ES``)."""

    display_name: str = Field(alias="displayName")
    """Human-readable voice name."""

    display_gender: TtsVoiceDisplayGenderOrStr = Field(alias="displayGender")
    """Voice gender."""

    accent: OptionalNullable[str] = UNSET
    """Accent (e.g. ``american``, ``british``)."""

    description: OptionalNullable[str] = UNSET
    """Description of the voice."""

    supports_direct_tool_execution: bool = Field(alias="supportsDirectToolExecution")
    """When false, this voice cannot be used directly with ``POST /v1/tools/text-to-speech``. All voices, regardless of
    this field, can be used in full video generation workflows such as script-to-video."""

    supports_all_languages: bool = Field(alias="supportsAllLanguages")
    """When true, this voice can synthesize text in any language regardless of its ``languageCode``. When false, the
    voice only supports its listed language."""

    is_deprecated: bool = Field(alias="isDeprecated")
    """When true, this voice is deprecated and may be removed in a future API version. Prefer non-deprecated voices for
    new integrations."""


class TtsVoiceDict(TypedDict):
    voice_id: str
    language_code: str
    display_name: str
    display_gender: TtsVoiceDisplayGenderOrStr
    accent: NotRequired[str | None]
    description: NotRequired[str | None]
    supports_direct_tool_execution: bool
    supports_all_languages: bool
    is_deprecated: bool
