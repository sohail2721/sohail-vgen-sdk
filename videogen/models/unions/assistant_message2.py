from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..assistant_message import AssistantMessage, AssistantMessageDict
from ..assistant_message1 import AssistantMessage1, AssistantMessage1Dict

AssistantMessage2: TypeAlias = Annotated[
    Annotated[AssistantMessage, Tag("user")] | Annotated[AssistantMessage1, Tag("assistant")], WireDiscriminator("role")
]
"""A single message in an assistant chat. Discriminated by ``role``."""

AssistantMessage2Dict: TypeAlias = AssistantMessageDict | AssistantMessage1Dict
