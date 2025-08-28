from typing import Any, Literal, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
   # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    app_name: str = "My Notes App"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str ="Note App"

    RATE_LIMIT: str = "1/second"
    PAGINATION_LIMIT: int = 5

    def all_cors_origins(self) -> list[str]:
        return ["*"]

settings = Settings()