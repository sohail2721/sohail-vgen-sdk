from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .aspect_ratio import AspectRatio, AspectRatioDict
from .enums.model_quality3 import ModelQuality3OrStr
from .unions.remix_action15 import RemixAction15, RemixAction15Dict
from .workflow_caption_style import WorkflowCaptionStyle, WorkflowCaptionStyleDict


class SlideshowToVideoRequest(SdkBaseModel):
    file_id: str = Field(alias="fileId")
    """Opaque file id of an uploaded PDF or PowerPoint file (e.g. ``vg_file_...``). Upload the file first via ``POST
    /v1/files/upload``."""

    slide_scripts: Optional[list[str]] = Field(default=UNSET, alias="slideScripts")
    """Optional per-slide narration, in slide order, applied by index: each slide uses its matching entry, and an empty
    string makes that slide silent. If you provide fewer entries than slides, the remaining slides are silent; extra
    entries are ignored. Omit this field entirely to narrate each slide from its speaker notes in the uploaded file. To
    guarantee no narration on any slide, pass an empty array."""

    aspect_ratio: Optional[AspectRatio] = Field(default=UNSET, alias="aspectRatio")
    """Aspect ratio as a width:height pair (e.g. 16 and 9 for 16:9). Not pixel dimensions."""

    language: Optional[str] = UNSET
    """Output language as a BCP-47 code (e.g. ``en``, ``es``, ``fr``). Defaults to English."""

    voice_id: OptionalNullable[str] = Field(default=UNSET, alias="voiceId")
    """Catalog ``displayName`` (e.g. ``Matilda``) or voice id from ``GET /v1/resources/tts-voices`` (e.g.
    ``vg_voic_...``). A default voice is used when omitted. Any voice may be used here, including voices where
    ``supportsDirectToolExecution`` is false."""

    voice_speed: Optional[float] = Field(default=UNSET, alias="voiceSpeed")
    """Speech rate multiplier, between 0.5 (half speed) and 2 (double speed). Defaults to the voice's default speed."""

    actor_entity_id: OptionalNullable[str] = Field(default=UNSET, alias="actorEntityId")
    """Recommended. Optional id of a built-in stock actor or an ACTOR entity (e.g. ``vg_enti_...``) with an image
    reference. When set, narration is delivered by that actor avatar. Omit or pass ``null`` for voiceover without an
    avatar."""

    avatar_quality: Optional[ModelQuality3OrStr] = Field(default=UNSET, alias="avatarQuality")
    """Avatar generation quality tier. Applies when ``actorEntityId`` is provided. Optional; when omitted, your
    account's Default AI quality for avatars is used."""

    slideshow_theme_entity_id: Optional[str] = Field(default=UNSET, alias="slideshowThemeEntityId")
    """Optional id of a SLIDESHOW_THEME entity (e.g. ``vg_enti_...``) whose reference board defines the shared slide
    design system (fonts, colors, layout) applied to generated or edited slides. Create one via ``POST /v1/entities``
    with ``entityType`` SLIDESHOW_THEME and attach a reference image or a PDF / PowerPoint. Omit when converting an
    uploaded deck's original pages into a video; VideoGen derives a theme from those pages in the background so later
    edits can match the original slides."""

    caption_style: OptionalNullable[WorkflowCaptionStyle] = Field(default=UNSET, alias="captionStyle")
    """Caption styling. Omit to use the default style with captions shown. Pass an object to override individual style
    fields (any omitted field uses the default). Pass ``null`` to hide captions entirely."""

    logo_file_id: OptionalNullable[str] = Field(default=UNSET, alias="logoFileId")
    """Optional file id of an uploaded logo image to overlay on the video (e.g. ``vg_file_...``). Upload the image first
    via ``POST /v1/files/upload``. Only image files are accepted."""

    remix_actions: Optional[list[RemixAction15]] = Field(default=UNSET, alias="remixActions")
    """Optional edits applied to the project after the video is built, in order. Each action runs asynchronously; the
    response returns one remix action id per action. Captions and a logo are set with the ``captionStyle`` and
    ``logoFileId`` request fields above; recommended remix actions here are ``CONVERT_IMAGES_TO_VIDEOS`` to animate
    still images into clips, and ``ADD_TRANSITIONS`` to stamp transitions between sections and assets. See the `Remix
    actions </remix-actions>`__ guide."""

    is_output_temporary: bool = Field(default=False, alias="isOutputTemporary")
    """When true, the video's generated OUTPUT files (AI images, video clips, voiceover audio, avatars) are created as
    temporary: guaranteed available for 24 hours, after which they may be archived and later deleted. This also covers
    files produced by post-build remix actions (e.g. generated background music, image-to-video conversions). Use this
    when your integration downloads or re-hosts the results itself and does not need VideoGen to retain them. The
    project and its metadata are unaffected. Defaults to false."""

    hide_from_ui: bool = Field(default=False, alias="hideFromUi")
    """When true, generated files are hidden from the VideoGen Media page by default. They remain accessible through the
    API. Defaults to false."""


class SlideshowToVideoRequestDict(TypedDict):
    file_id: str
    slide_scripts: NotRequired[list[str]]
    aspect_ratio: NotRequired[AspectRatioDict]
    language: NotRequired[str]
    voice_id: NotRequired[str | None]
    voice_speed: NotRequired[float]
    actor_entity_id: NotRequired[str | None]
    avatar_quality: NotRequired[ModelQuality3OrStr]
    slideshow_theme_entity_id: NotRequired[str]
    caption_style: NotRequired[WorkflowCaptionStyleDict | None]
    logo_file_id: NotRequired[str | None]
    remix_actions: NotRequired[list[RemixAction15Dict]]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
