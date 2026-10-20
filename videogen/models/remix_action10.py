from __future__ import annotations

from typing import Literal

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RemixAction10(SdkBaseModel):
    """Sharpen every eligible asset in the project up to 4K, replacing each in place. Runs asynchronously: one upscaled
    asset is generated per eligible asset. If the project has no eligible assets, the action is skipped and completes
    successfully without changing anything."""

    type_: Literal["UPSCALE_ASSETS"] = Field(default="UPSCALE_ASSETS", alias="type")
    """Discriminator value: UPSCALE_ASSETS"""

    include_videos: OptionalNullable[bool] = Field(default=UNSET, alias="includeVideos")
    """Also upscale video assets (billed per output second). Defaults to ``true``."""

    include_stock_content: OptionalNullable[bool] = Field(default=UNSET, alias="includeStockContent")
    """Also upscale stock (library) assets, not just uploaded or generated ones. Defaults to ``true``."""


class RemixAction10Dict(TypedDict):
    type_: Literal["UPSCALE_ASSETS"]
    include_videos: NotRequired[bool | None]
    include_stock_content: NotRequired[bool | None]
