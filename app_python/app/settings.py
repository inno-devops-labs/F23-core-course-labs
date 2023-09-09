"""
Application settings handled using Pydantic Settings management.

Pydantic is used both to read app settings from various sources,
and to validate their values.

https://docs.pydantic.dev/latest/usage/settings/
"""
from pydantic import BaseModel, BaseSettings


class APIInfo(BaseModel):
    title = "time-app API"
    version = "0.0.1"


class App(BaseModel):
    show_error_details = False


class Settings(BaseSettings):
    # to override info:
    # export app_info='{"title": "x", "version": "0.0.2"}'
    info: APIInfo = APIInfo()

    # to override app:
    # export app_app='{"show_error_details": True}'
    app: App = App()

    class Config:
        env_prefix = "APP_"  # defaults to no prefix, i.e. ""


def load_settings() -> Settings:
    return Settings()
