from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class PronunciationReplacement(SdkBaseModel):
    original: str
    replacement: str


class PronunciationReplacementDict(TypedDict):
    original: str
    replacement: str
