from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .error_requirement import ErrorRequirement, ErrorRequirementDict


class ApiErrorModel(SdkBaseModel):
    """Standard error body returned with every non-2xx response (the ``default`` response of every operation). The HTTP
    status code conveys the error class; this body carries the details:

    - ``400`` invalid request, ``401`` missing or invalid API key, ``403`` not permitted (e.g. plan or add-on required,
        see ``requirement``), ``404`` not found, ``409`` conflict, ``429`` rate limited or out of credits, ``5xx``
        server error.

    Common ``code`` values include ``invalid_request``, ``invalid_api_key``, ``not_authorized``, ``not_found``,
    ``insufficient_credits``, and ``rate_limited``. Always branch on ``code`` (and ``requirement.type`` when present)
    rather than parsing ``message``."""

    message: str
    """Human-readable error description. For display and logging only; do not branch on its exact text."""

    code: OptionalNullable[str] = UNSET
    """Machine-readable error code in snake_case (e.g. ``invalid_api_key``, ``insufficient_credits``). ``null`` when no
    specific code applies."""

    requirement: OptionalNullable[ErrorRequirement] = UNSET
    """What is needed to resolve the error. Present when the error can be fixed by fulfilling a specific requirement
    (e.g. purchasing an add-on); ``null`` otherwise."""

    internal_error_code: OptionalNullable[str] = Field(default=UNSET, alias="internalErrorCode")
    """Opaque internal error code for debugging. Include this when contacting support. ``null`` when not applicable."""


class ApiErrorModelDict(TypedDict):
    message: str
    code: NotRequired[str | None]
    requirement: NotRequired[ErrorRequirementDict | None]
    internal_error_code: NotRequired[str | None]
