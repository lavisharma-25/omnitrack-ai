from pathlib import Path
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """
    Application configuration loaded from environment variables.
    """
    
    # --- LLM CONFIG ---
    OPENAI_API_KEY: str
    OPENAI_MODEL: str = "gpt-4o"

    # --- APP CONFIG ---
    APP_NAME: str = "TrackFlow AI"
    APP_ENV: str = "dev"
    DEBUG: bool = False

    # --- STORAGE ---
    STORAGE_DIR: Path = BASE_DIR / "app" / "storage" / "trackers"

    # --- LOGGING ---
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    def ensure_dirs(self):
        """Ensure required directories exist."""
        self.STORAGE_DIR.mkdir(parents=True, exist_ok=True)


@lru_cache()
def get_settings() -> Settings:
    """
    Cached settings instance (singleton pattern).
    """
    settings = Settings()
    settings.ensure_dirs()
    return settings



# import os
# from pathlib import Path
# from typing import Optional
# from dotenv import load_dotenv
# from functools import lru_cache
# from google.oauth2 import service_account

# from app.utils.load_creds import load_json_path

# BASE_DIR = Path(__file__).resolve().parents[1]

# load_dotenv(BASE_DIR / ".env", override=True)

# class Settings:
#     def __init__(self) -> None:
#         self.environment: str = os.getenv("ENVIRONMENT", "development")
#         self.debug: bool = self.environment.lower() == "development"

#         self.port: int = int(os.getenv("PORT", "8000"))

#         self.logs_dir: Path = BASE_DIR / "logs"
#         self.data_dir: Path = BASE_DIR / "data" / "trackers"

#         self.gemini_api_key: str = self._required_env("GEMINI_API_KEY")

#         self.gemini_model_flash: str = os.getenv("GEMINI_MODEL_FLASH", "gemini-2.5-flash")

#         self.gemini_model_lite: str = os.getenv("GEMINI_MODEL_LITE", "gemini-2.5-flash-lite")

#         self.location: str = os.getenv("LOCATION", "")

#         self.tmdb_api_key: Optional[str] = os.getenv("TMDB_API_KEY")

#         self.tmdb_base_url: str = os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")

#         self.service_account_path: Optional[str] = load_json_path("model_credentials")

#         self.service_account_scopes = ["https://www.googleapis.com/auth/cloud-platform"]

#     @staticmethod
#     def _required_env(key: str) -> str:
#         value = os.getenv(key)

#         if not value:
#             raise ValueError(
#                 f"Missing required environment variable: {key}"
#             )

#         return value

#     @property
#     def credentials(self):
#         if not self.service_account_path:
#             raise ValueError(
#                 "Google service account credentials file not found."
#             )

#         return service_account.Credentials.from_service_account_file(
#             self.service_account_path,
#             scopes=self.service_account_scopes,
#         )

#     def create_directories(self) -> None:
#         self.logs_dir.mkdir(parents=True, exist_ok=True)
#         self.data_dir.mkdir(parents=True, exist_ok=True)


# @lru_cache
# def get_settings() -> Settings:
#     return Settings()


# settings = get_settings()