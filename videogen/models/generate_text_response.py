from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateTextResponse(SdkBaseModel):
    text: str
    """The generated text."""


class GenerateTextResponseDict(TypedDict):
    text: str
