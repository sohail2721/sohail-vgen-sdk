from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class RemixActionType(str, Enum):
    """The kind of edit a remix action applies."""

    SET_BACKGROUND_MUSIC = "SET_BACKGROUND_MUSIC"
    SET_LOGO = "SET_LOGO"
    ENABLE_CAPTIONS = "ENABLE_CAPTIONS"
    DISABLE_CAPTIONS = "DISABLE_CAPTIONS"
    ADD_TRANSITIONS = "ADD_TRANSITIONS"
    ADD_ZOOM = "ADD_ZOOM"
    RESIZE_PROJECT = "RESIZE_PROJECT"
    CLEAN_UP_TRANSCRIPT = "CLEAN_UP_TRANSCRIPT"
    CONVERT_IMAGES_TO_VIDEOS = "CONVERT_IMAGES_TO_VIDEOS"
    REGENERATE_IMAGES = "REGENERATE_IMAGES"
    UPSCALE_ASSETS = "UPSCALE_ASSETS"
    CHANGE_NARRATOR = "CHANGE_NARRATOR"
    SHUFFLE_STOCK_VISUALS = "SHUFFLE_STOCK_VISUALS"
    GENERATE_MUSIC = "GENERATE_MUSIC"
    TRANSLATE_PROJECT = "TRANSLATE_PROJECT"

    __str__ = str.__str__


RemixActionTypeOrStr: TypeAlias = Annotated[RemixActionType | str, open_enum_validator(RemixActionType)]
