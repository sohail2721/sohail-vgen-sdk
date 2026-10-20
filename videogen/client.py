from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.account import Account
from .apis.assistant import Assistant
from .apis.entities import Entities
from .apis.files import Files
from .apis.projects import Projects
from .apis.resources import Resources
from .apis.text import Text
from .apis.tools import Tools
from .apis.webhooks import Webhooks
from .apis.workflows import Workflows
from .auth import AuthSchemes
from .base_client import DEFAULT_TIMEOUT, BaseVideogenClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    BearerAuthScheme,
    HttpClient,
    Httpx2Client,
    LoggingOptionsOrDict,
    RawClient,
    RetryOptionsOrDict,
    no_auth,
    param,
)


class VideogenClient(BaseVideogenClient[RawClient]):
    def __init__(
        self,
        *,
        base_url: str | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        bearer_auth: str | None = None,
    ) -> None:
        super().__init__(
            base_url=base_url, timeout=timeout, retry_options=retry_options, logging_options=logging_options
        )
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
            retry_options=self._retry_options,
            logging_options=self._logging_options,
            global_headers=[
                param[str]("User-Agent", "VideogenClient/1.0.0 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "1.0.0"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AuthSchemes(bearer_auth=BearerAuthScheme(bearer_auth) if bearer_auth is not None else no_auth)

    @cached_property
    def account(self) -> Account:
        return Account(self._raw_client, self._server, self._auth)

    @cached_property
    def assistant(self) -> Assistant:
        return Assistant(self._raw_client, self._server, self._auth)

    @cached_property
    def entities(self) -> Entities:
        return Entities(self._raw_client, self._server, self._auth)

    @cached_property
    def files(self) -> Files:
        return Files(self._raw_client, self._server, self._auth)

    @cached_property
    def projects(self) -> Projects:
        return Projects(self._raw_client, self._server, self._auth)

    @cached_property
    def resources(self) -> Resources:
        return Resources(self._raw_client, self._server, self._auth)

    @cached_property
    def text(self) -> Text:
        return Text(self._raw_client, self._server, self._auth)

    @cached_property
    def tools(self) -> Tools:
        return Tools(self._raw_client, self._server, self._auth)

    @cached_property
    def webhooks(self) -> Webhooks:
        return Webhooks(self._raw_client, self._server, self._auth)

    @cached_property
    def workflows(self) -> Workflows:
        return Workflows(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = VideogenClient
