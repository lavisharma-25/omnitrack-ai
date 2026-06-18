import os
from pathlib import Path
from typing import Optional
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from google.oauth2 import service_account

from src.utils.load_creds import load_json_path

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # --- APP CONFIG ---
    APP_NAME: str = "TrackFlow AI"
    APP_ENV: str = "development"

    # --- LOGGING ---
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    LOGS_DIR: Path = (BASE_DIR / "LOGS")
    
    # --- LLM CONFIG ---
    GEMINI_MODEL_FLASH: str = "gemini-2.5-flash"
    GEMINI_MODEL_LITE: str = "gemini-2.5-flash-lite"
    LOCATION: str = "global"
    SERVICE_ACCOUNT_PATH: Optional[str] = load_json_path("model_credentials")
    SERVICE_ACCOUNT_SCOPES: list[str] = ["https://www.googleapis.com/auth/cloud-platform"]

    TMDB_API_KEY: Optional[str] = os.getenv("TMDB_API_KEY")
    TMDB_BASE_URL: str = os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")

    # --- STORAGE ---
    STORAGE_DIR: Path = (BASE_DIR / "src" / "storage")
    TRACKERS_DIR: Path = (STORAGE_DIR / "trackers")
    REGISTRY_FILE: Path = (STORAGE_DIR / "tracker_registry.json")
    SCHEMA_FILE: Path = (STORAGE_DIR / "schema_registry.json")

    def ensure_dirs(self):
        """Ensure required directories exist."""
        self.LOGS_DIR.mkdir(parents=True, exist_ok=True)
        self.STORAGE_DIR.mkdir(parents=True, exist_ok=True)
        self.TRACKERS_DIR.mkdir(parents=True, exist_ok=True)
        self.REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
        self.SCHEMA_FILE.parent.mkdir(parents=True, exist_ok=True)

    @property
    def credentials(self):
        if not self.SERVICE_ACCOUNT_PATH:
            raise ValueError("Google service account credentials file not found.")

        return service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_PATH,
            scopes=self.SERVICE_ACCOUNT_SCOPES,
        )


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings instance (singleton pattern).
    """
    settings = Settings()
    settings.ensure_dirs()
    return settings

settings = get_settings()

# for key, value in settings.model_dump().items():
#     print(f"{key}: {value}")