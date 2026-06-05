from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Sentiora AI"
    APP_VERSION: str = "0.1.0"
    APP_ENV: str = "development"
    DEBUG: bool = True

    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000

    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    LOG_LEVEL: str = "INFO"

    PROJECT_DESCRIPTION: str = (
        "AI-powered crisis intelligence and situational awareness platform."
    )

    API_V1_PREFIX: str = "/api/v1"

    REQUEST_TIMEOUT_SECONDS: int = 30

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )
    POSTGRES_USER: str = "sentiora"
    POSTGRES_PASSWORD: str = "sentiora_password"
    POSTGRES_DB: str = "sentiora_db"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
