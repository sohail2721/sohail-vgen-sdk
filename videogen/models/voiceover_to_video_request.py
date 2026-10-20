from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .aspect_ratio import AspectRatio, AspectRatioDict
from .enums.model_quality3 import ModelQuality3OrStr
from .enums.model_quality4 import ModelQuality4OrStr
from .enums.visual_pacing import VisualPacing, VisualPacingOrStr
from .scene_description_range import SceneDescriptionRange, SceneDescriptionRangeDict
from .unions.remix_action15 import RemixAction15, RemixAction15Dict
from .workflow_caption_style import WorkflowCaptionStyle, WorkflowCaptionStyleDict
from .workflow_visual_style import WorkflowVisualStyle, WorkflowVisualStyleDict


class VoiceoverToVideoRequest(SdkBaseModel):
    file_id: str = Field(alias="fileId")
    """Opaque file id of an uploaded voiceover audio file (e.g. ``vg_file_...``). Upload the file first via ``POST
    /v1/files/upload``. Attach a pre-computed transcript at upload time (via the ``transcript`` field on ``POST
    /v1/files/upload``) to skip re-transcription."""

    scenes: Optional[list[SceneDescriptionRange]] = UNSET
    """Optional timed scene descriptions guiding what to show on screen during each absolute time range of the video.
    Ranges must be sorted by ``startSeconds`` and non-overlapping. Omit to let the workflow choose visuals
    automatically."""

    aspect_ratio: Optional[AspectRatio] = Field(default=UNSET, alias="aspectRatio")
    """Aspect ratio as a width:height pair (e.g. 16 and 9 for 16:9). Not pixel dimensions."""

    visual_style: WorkflowVisualStyle = Field(alias="visualStyle")
    """Visual style for the generated b-roll."""

    visual_pacing: VisualPacingOrStr = Field(default=VisualPacing.MEDIUM, alias="visualPacing")
    """How quickly visuals change. FAST shows more, shorter shots; SLOW holds each visual longer. Defaults to MEDIUM."""

    quality: Optional[ModelQuality4OrStr] = UNSET
    """Image generation quality tier for AI-generated visuals. Optional; when omitted, your account's Default AI quality
    for images is used (change it at https://app.videogen.io/settings/account). Only applies when ``visualStyle.type``
    is AI_IMAGE; STOCK pulls existing footage and is unaffected."""

    language: Optional[str] = UNSET
    """Output language as a BCP-47 code (e.g. ``en``, ``es``, ``fr``). Defaults to English."""

    actor_entity_id: OptionalNullable[str] = Field(default=UNSET, alias="actorEntityId")
    """Recommended. Optional id of a built-in stock actor or an ACTOR entity (e.g. ``vg_enti_...``) with an image
    reference. When set, narration is delivered by that actor avatar. Omit or pass ``null`` for voiceover without an
    avatar."""

    avatar_quality: Optional[ModelQuality3OrStr] = Field(default=UNSET, alias="avatarQuality")
    """Avatar generation quality tier. Applies when ``actorEntityId`` is provided. Optional; when omitted, your
    account's Default AI quality for avatars is used."""

    caption_style: OptionalNullable[WorkflowCaptionStyle] = Field(default=UNSET, alias="captionStyle")
    """Caption styling. Omit to use the default style with captions shown. Pass an object to override individual style
    fields (any omitted field uses the default). Pass ``null`` to hide captions entirely."""

    logo_file_id: OptionalNullable[str] = Field(default=UNSET, alias="logoFileId")
    """Optional file id of an uploaded logo image to overlay on the video (e.g. ``vg_file_...``). Upload the image first
    via ``POST /v1/files/upload``. Only image files are accepted."""

    workflow_agent_context: Optional[str] = Field(default=UNSET, alias="workflowAgentContext")
    """Optional production notes for the AI that builds the video — visual direction for how to illustrate the voiceover
    (e.g. on-screen code or text to display, specific b-roll to feature, or scene-by-scene staging). Never spoken; does
    not change the uploaded voiceover audio or its transcript."""

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


class VoiceoverToVideoRequestDict(TypedDict):
    file_id: str
    scenes: NotRequired[list[SceneDescriptionRangeDict]]
    aspect_ratio: NotRequired[AspectRatioDict]
    visual_style: WorkflowVisualStyleDict
    visual_pacing: NotRequired[VisualPacingOrStr]
    quality: NotRequired[ModelQuality4OrStr]
    language: NotRequired[str]
    actor_entity_id: NotRequired[str | None]
    avatar_quality: NotRequired[ModelQuality3OrStr]
    caption_style: NotRequired[WorkflowCaptionStyleDict | None]
    logo_file_id: NotRequired[str | None]
    workflow_agent_context: NotRequired[str]
    remix_actions: NotRequired[list[RemixAction15Dict]]
    is_output_temporary: NotRequired[bool]
    hide_from_ui: NotRequired[bool]
