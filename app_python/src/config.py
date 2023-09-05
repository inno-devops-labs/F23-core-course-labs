from pydantic_settings import BaseSettings


class Config(BaseSettings):
    PORT: int = 5000
