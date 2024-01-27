import pathlib
import time
from threading import Lock
from typing import TypedDict, Literal, TypeAlias

from attrs import define
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from robot.api import logger
from robot.api.deco import library, keyword

from .config import auth_settings

ConfigKeys: TypeAlias = Literal["cert_path", "client_id", "client_secret", "token_url"]


class AuthError(Exception):
    pass


class AuthHeader(TypedDict):
    Authorization: str


@define
class AuthHandlerConfig:
    client_id: str
    client_secret: str
    token_url: str
    verify: pathlib.Path | None

    @classmethod
    def from_dict(cls, _dict: dict[ConfigKeys, str]) -> "AuthHandlerConfig":
        try:
            client_id = _dict["client_id"]
            client_secret = _dict["client_secret"]
            token_url = _dict["token_url"]

            cert_path = _dict.get("cert_path")
            verify = None if cert_path is None else pathlib.Path(cert_path)

            if verify is not None and not verify.exists():
                raise AuthError(
                    f"No certificate is found in the provided path: {verify}"
                )

        except (AuthError, KeyError) as exc:
            raise AuthError("Invalid AuthHandler configuration") from exc

        return cls(
            client_id=client_id,
            client_secret=client_secret,
            token_url=token_url,
            verify=verify,
        )


class AuthHandler:
    def __init__(self, config: AuthHandlerConfig) -> None:
        self._token_update_time: int | None = None

        self.config = config
        self.oauth_client = BackendApplicationClient(client_id=config.client_id)
        self.session = OAuth2Session(client=self.oauth_client)

        self.lock = Lock()

    @property
    def access_token(self) -> str:
        return self.session.access_token

    @property
    def expires_in(self) -> int:
        return self.oauth_client.expires_in

    @property
    def token_update_time(self) -> int | None:
        return self._token_update_time

    @token_update_time.setter
    def token_update_time(self, value: int) -> None:
        self._token_update_time = value

    def _fetch_access_token(self) -> None:
        logger.debug("Start fetching new access token")
        try:
            self.session.fetch_token(
                token_url=self.config.token_url,
                client_id=self.config.client_id,
                client_secret=self.config.client_secret,
                verify=self.config.verify,
            )
            self.token_update_time = int(time.time())

        except Exception as exc:
            raise AuthError(f"Failed to retrieve auth token {exc}") from exc

    def _is_token_about_to_expire(self) -> bool:
        if self.access_token is None or self.token_update_time is None:
            return True

        else:
            time_elapsed = int(time.time()) - self.token_update_time
            logger.debug(
                f"Token expiration info: token_update_time: {self.token_update_time}, "
                f"expires_in: {self.expires_in}, time_elapsed: {time_elapsed}"
            )
            return self.expires_in < (time_elapsed + 60)

    def get_access_token(self, force_new: bool = False) -> str:
        with self.lock:
            if force_new or self.token_update_time is None:
                self._fetch_access_token()
                return self.access_token

            if self._is_token_about_to_expire():
                self._fetch_access_token()

            return self.access_token

    def get_auth_header(self, force_new: bool = False) -> AuthHeader:
        return {"Authorization": f"Bearer {self.get_access_token(force_new)}"}


@library(scope="GLOBAL")
class AuthLibrary:
    def __init__(self) -> None:
        self.auth_handler = AuthHandler(
            config=AuthHandlerConfig(
                client_id=auth_settings.CLIENT_ID,
                client_secret=auth_settings.CLIENT_SECRET,
                token_url=auth_settings.TOKEN_URL,
                verify=auth_settings.VERIFY,
            )
        )

    @keyword
    def get_auth_header(self, force_new: bool = False) -> AuthHeader:
        return self.auth_handler.get_auth_header(force_new)
