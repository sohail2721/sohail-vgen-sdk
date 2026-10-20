from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .aspect_ratio4 import AspectRatio4, AspectRatio4Dict
from .motion_graphic_sub_tool_modes1 import MotionGraphicSubToolModes1, MotionGraphicSubToolModes1Dict


class GenerateMotionGraphicRequest(SdkBaseModel):
    prompt: str
    """Text prompt describing the animated motion graphic to generate. Describe the on-screen elements, any text and how
    it should animate, and the overall motion in plain language."""

    file_ids: Optional[list[str]] = Field(default=UNSET, alias="fileIds")
    """Optional file ids of uploaded reference media (images, videos, or audio) the motion graphic may display or
    animate (e.g. ``["vg_file_..."]``). Upload files first via ``POST /v1/files/upload``, then pass the returned ids
    here."""

    entity_ids: Optional[list[str]] = Field(default=UNSET, alias="entityIds")
    """Optional actor, product, or visual-style entity ids (e.g. ``["vg_enti_..."]``). The motion graphic uses each
    entity as identity/reference the same way in-app motion graphic generation does. Can be combined with ``fileIds``.
    Mentions in ``prompt`` are also collected. A missing id returns not found; an inaccessible id returns a permission
    error."""

    duration_seconds: OptionalNullable[int] = Field(default=UNSET, alias="durationSeconds")
    """Desired length of the motion graphic in seconds, a whole number between 1 and 300. When omitted, the duration is
    chosen automatically to fit the prompt (recommended)."""

    aspect_ratio: Optional[AspectRatio4] = Field(default=UNSET, alias="aspectRatio")
    """Aspect ratio for the generated motion graphic. Defaults to 16:9 when omitted."""

    transparent_background: bool = Field(default=True, alias="transparentBackground")
    """When true, renders the motion graphic with a transparent background as a WebM video suitable for overlaying on
    other video or images. Set to false for an opaque MP4. Defaults to true."""

    sub_tool_modes: Optional[MotionGraphicSubToolModes1] = Field(default=UNSET, alias="subToolModes")
    """Optional per-capability controls for the media the motion graphic may generate or fetch (generated images,
    generated video clips, generated voiceover, and stock media search). Each capability is AUTO, ENABLED, or DISABLED.
    Omit to use AUTO for every capability."""

    num_results: int = Field(default=1, alias="numResults")
    """Number of output results to generate. Defaults to 1."""

    is_output_temporary: bool = Field(default=False, alias="isOutputTemporary")
    """When true, generated files are temporary. Temporary files are guaranteed to be available for 24 hours, after
    which they may be archived at any time. Temporary files are not analyzed (no description, transcript, or embedding
    will be generated), so they will not appear in search results. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, generated files are hidden from the VideoGen Media page by default. They remain accessible through the
    API. Defaults to false."""


class GenerateMotionGraphicRequestDict(TypedDict):
    prompt: str
    file_ids: NotRequired[list[str]]
    entity_ids: NotRequired[list[str]]
    duration_seconds: NotRequired[int | None]
    aspect_ratio: NotRequired[AspectRatio4Dict]
    transparent_background: NotRequired[bool]
    sub_tool_modes: NotRequired[MotionGraphicSubToolModes1Dict]
    num_results: NotRequired[int]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
