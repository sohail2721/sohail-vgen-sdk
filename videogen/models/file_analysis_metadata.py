from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.file_analysis_metadata_analysis_loading_state import FileAnalysisMetadataAnalysisLoadingStateOrStr


class FileAnalysisMetadata(SdkBaseModel):
    """Background analysis state for a file. Background analysis populates ``description``, ``transcript``,
    ``durationSeconds``, and the search embedding after a file is uploaded or generated; this object lets you render a
    progress indicator while it runs (and skip rendering once it's done)."""

    analysis_loading_state: FileAnalysisMetadataAnalysisLoadingStateOrStr = Field(alias="analysisLoadingState")
    """Coarse-grained analysis state.

    - ``UNATTEMPTED``: analysis has not started yet.
    - ``LOADING``: analysis is in progress.
    - ``FULFILLED``: analysis completed successfully. ``description``, ``transcript``, and ``durationSeconds`` are now
        populated where applicable for the file's type.
    - ``REJECTED``: analysis failed permanently and will not be retried."""

    analysis_progress_percentage: float = Field(alias="analysisProgressPercentage")
    """Progress in ``[0, 100]``. Always ``100`` when ``analysisLoadingState`` is ``FULFILLED``. Otherwise the most
    recent in-flight progress reported by the analysis task (or ``0`` if no progress has been reported yet)."""

    analysis_attempt_index: Optional[int] = Field(default=UNSET, alias="analysisAttemptIndex")
    """Zero-based index of the current analysis task attempt. Only present while analysis is still loading
    (``UNATTEMPTED`` or ``LOADING``); omitted once analysis reaches a terminal state."""


class FileAnalysisMetadataDict(TypedDict):
    analysis_loading_state: FileAnalysisMetadataAnalysisLoadingStateOrStr
    analysis_progress_percentage: float
    analysis_attempt_index: NotRequired[int]
