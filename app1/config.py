import os
from pathlib import Path
from dotenv import load_dotenv
from google.oauth2 import service_account
from app1.utils.load_creds import load_json_path


load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data" / "trackers"
DATA_DIR.mkdir(parents=True, exist_ok=True)

APP_NAME = "TrackFlow AI"
APP_VERSION = "0.1.0"
port = int(os.getenv("PORT", 8000))

gemini_api_key = os.getenv("GEMINI_API_KEY", "")
gemini_model_flash = os.getenv("GEMINI_MODEL_FLASH", "gemini-2.5-flash")
gemini_model_lite = os.getenv("GEMINI_MODEL_LITE", "gemini-2.5-flash-lite")
location = os.getenv("LOCATION", "")
service_account_file_path = load_json_path("model_credentials")
service_account_scope = ["https://www.googleapis.com/auth/cloud-platform"]
credentials = service_account.Credentials.from_service_account_file(service_account_file_path,scopes=service_account_scope)

TMDB_API_KEY = os.getenv("TMDB_API_KEY")
TMDB_BASE_URL = os.getenv("TMDB_BASE_URL", "https://api.themoviedb.org/3")
TRACKFLOW_DATA_PATH = Path(
    os.getenv("TRACKFLOW_DATA_PATH", BASE_DIR / "app" / "storage" / "data.json")
)

# Backward-compatible aliases for the original scaffold.
file_path = TRACKFLOW_DATA_PATH
