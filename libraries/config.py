import os
import pathlib

from pydantic import field_validator, ValidationError
from pydantic_core import Url
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    CLIENT_ID: str = "dummy_client"
    CLIENT_SECRET: str = "dummy_secret"
    TOKEN_URL: str = "https://auth.dummy.tinaa.tlabs.ca/token"
    VERIFY: str = str(pathlib.Path(__file__).parents[1] / "cacerts/root.pem")

    @field_validator("TOKEN_URL")
    def check_token_url(cls, value: str) -> str:
        try:
            Url(value)
        except ValidationError:
            raise ValueError("TOKEN_URL must be a valid URL")

        return value

    @field_validator("VERIFY")
    def check_verify_path_exists(cls, value: str) -> str:
        cert_path = pathlib.Path(value)

        if not cert_path.exists():
            raise ValueError(
                f"No file found in the provided path: {value}, {os.getcwd()}"
            )

        return value


auth_settings = AuthSettings()


class Environment(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    BASE_URL: str = "http://localhost:8080"

    @field_validator("BASE_URL")
    def check_base_url(cls, value: str) -> str:
        try:
            Url(value)
        except ValidationError:
            raise ValueError("BASE_URL must be a valid URL")

        return value


environment = Environment()
