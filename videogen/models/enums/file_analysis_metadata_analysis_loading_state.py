from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileAnalysisMetadataAnalysisLoadingState(str, Enum):
    """Coarse-grained analysis state.

    - ``UNATTEMPTED``: analysis has not started yet.
    - ``LOADING``: analysis is in progress.
    - ``FULFILLED``: analysis completed successfully. ``description``, ``transcript``, and ``durationSeconds`` are now
        populated where applicable for the file's type.
    - ``REJECTED``: analysis failed permanently and will not be retried."""

    UNATTEMPTED = "UNATTEMPTED"
    LOADING = "LOADING"
    FULFILLED = "FULFILLED"
    REJECTED = "REJECTED"

    __str__ = str.__str__


FileAnalysisMetadataAnalysisLoadingStateOrStr: TypeAlias = Annotated[
    FileAnalysisMetadataAnalysisLoadingState | str, open_enum_validator(FileAnalysisMetadataAnalysisLoadingState)
]
