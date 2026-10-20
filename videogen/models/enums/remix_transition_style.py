from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RemixTransitionStyle(str, Enum):
    """A transition applied at a boundary. ``DYNAMIC`` auto-varies the style across boundaries; ``NONE`` removes
    transitions; the rest apply that fixed style everywhere."""

    DYNAMIC = "DYNAMIC"
    NONE = "NONE"
    FADE = "FADE"
    RISE = "RISE"
    PAN = "PAN"
    POP = "POP"
    WIPE = "WIPE"

    __str__ = str.__str__


RemixTransitionStyleOrStr: TypeAlias = Annotated[RemixTransitionStyle | str, open_enum_validator(RemixTransitionStyle)]
