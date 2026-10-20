from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TtsVoiceDisplayGender(str, Enum):
    """Voice gender."""

    MALE = "MALE"
    FEMALE = "FEMALE"
    NEUTRAL = "NEUTRAL"

    __str__ = str.__str__


TtsVoiceDisplayGenderOrStr: TypeAlias = Annotated[
    TtsVoiceDisplayGender | str, open_enum_validator(TtsVoiceDisplayGender)
]
