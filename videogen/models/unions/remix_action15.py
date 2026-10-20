from __future__ import annotations

from typing import Annotated, TypeAlias

from pydantic import Tag

from ...core import WireDiscriminator
from ..remix_action import RemixAction, RemixActionDict
from ..remix_action1 import RemixAction1, RemixAction1Dict
from ..remix_action2 import RemixAction2, RemixAction2Dict
from ..remix_action3 import RemixAction3, RemixAction3Dict
from ..remix_action4 import RemixAction4, RemixAction4Dict
from ..remix_action5 import RemixAction5, RemixAction5Dict
from ..remix_action6 import RemixAction6, RemixAction6Dict
from ..remix_action7 import RemixAction7, RemixAction7Dict
from ..remix_action8 import RemixAction8, RemixAction8Dict
from ..remix_action9 import RemixAction9, RemixAction9Dict
from ..remix_action10 import RemixAction10, RemixAction10Dict
from ..remix_action11 import RemixAction11, RemixAction11Dict
from ..remix_action12 import RemixAction12, RemixAction12Dict
from ..remix_action13 import RemixAction13, RemixAction13Dict
from ..remix_action14 import RemixAction14, RemixAction14Dict

RemixAction15: TypeAlias = Annotated[
    (
        Annotated[RemixAction, Tag("SET_BACKGROUND_MUSIC")]
        | Annotated[RemixAction1, Tag("SET_LOGO")]
        | Annotated[RemixAction2, Tag("ENABLE_CAPTIONS")]
        | Annotated[RemixAction3, Tag("DISABLE_CAPTIONS")]
        | Annotated[RemixAction4, Tag("ADD_TRANSITIONS")]
        | Annotated[RemixAction5, Tag("ADD_ZOOM")]
        | Annotated[RemixAction6, Tag("RESIZE_PROJECT")]
        | Annotated[RemixAction7, Tag("CLEAN_UP_TRANSCRIPT")]
        | Annotated[RemixAction8, Tag("CONVERT_IMAGES_TO_VIDEOS")]
        | Annotated[RemixAction9, Tag("REGENERATE_IMAGES")]
        | Annotated[RemixAction10, Tag("UPSCALE_ASSETS")]
        | Annotated[RemixAction11, Tag("CHANGE_NARRATOR")]
        | Annotated[RemixAction12, Tag("SHUFFLE_STOCK_VISUALS")]
        | Annotated[RemixAction13, Tag("GENERATE_MUSIC")]
        | Annotated[RemixAction14, Tag("TRANSLATE_PROJECT")]
    ),
    WireDiscriminator("type"),
]
"""A single edit applied to a project. Each array entry is exactly one of the action types below, chosen by its ``type``
field; the variants are mutually-exclusive options, not fields you must all provide. Include only the actions you
want."""

RemixAction15Dict: TypeAlias = (
    RemixActionDict
    | RemixAction1Dict
    | RemixAction2Dict
    | RemixAction3Dict
    | RemixAction4Dict
    | RemixAction5Dict
    | RemixAction6Dict
    | RemixAction7Dict
    | RemixAction8Dict
    | RemixAction9Dict
    | RemixAction10Dict
    | RemixAction11Dict
    | RemixAction12Dict
    | RemixAction13Dict
    | RemixAction14Dict
)
