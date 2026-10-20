from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .language import Language, LanguageDict


class LanguageListResponse(SdkBaseModel):
    languages: list[Language]


class LanguageListResponseDict(TypedDict):
    languages: list[LanguageDict]
