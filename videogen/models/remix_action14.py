from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RemixAction14(SdkBaseModel):
    """Translate the whole project into another language: every piece of text (title, section names, on-screen text
    overlays, transcripts, and narration scripts) is translated, and — unless disabled — each AI voiceover is
    re-narrated in the new language. Runs asynchronously. Requires a Pro subscription. Retrieve the list of supported
    language codes from ``GET /v1/resources/languages``."""

    type_: Literal["TRANSLATE_PROJECT"] = Field(default="TRANSLATE_PROJECT", alias="type")
    """Discriminator value: TRANSLATE_PROJECT"""

    language_code: str = Field(alias="languageCode")
    """Target language code to translate the project into (e.g. ``es``, ``fr``, ``ja``). Must be one of the codes
    returned by ``GET /v1/resources/languages``."""

    change_voice: OptionalNullable[bool] = Field(default=UNSET, alias="changeVoice")
    """Swap each AI voiceover to a voice that natively matches the target language. Recommended, since keeping the
    original voice usually produces a foreign accent. Defaults to ``true``."""

    translate_image_text: OptionalNullable[bool] = Field(default=UNSET, alias="translateImageText")
    """Also re-generate every eligible image so that text baked into the image is translated too (image-to-image).
    Billed per generated image. Defaults to ``false``."""


class RemixAction14Dict(TypedDict):
    type_: Literal["TRANSLATE_PROJECT"]
    language_code: str
    change_voice: NotRequired[bool | None]
    translate_image_text: NotRequired[bool | None]
