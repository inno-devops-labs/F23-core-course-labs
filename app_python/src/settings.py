from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_port: int = 8000

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
