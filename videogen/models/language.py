from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Language(SdkBaseModel):
    """A language a project can be translated into."""

    language_code: str = Field(alias="languageCode")
    """The language code to pass to a ``TRANSLATE_PROJECT`` remix action (e.g. ``es``, ``fr``, ``ja``)."""

    name: str
    """Human-readable English name of the language (e.g. ``Spanish``)."""


class LanguageDict(TypedDict):
    language_code: str
    name: str
