from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    HOST: str = "0.0.0.0"
    PORT: int = 8000
    SECRET_KEY: str
    POSTGRES_URI: str


@lru_cache()
def get_settings() -> Settings:
    return Settings()  # type: ignore


settings = get_settings()
