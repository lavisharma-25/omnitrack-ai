from app1.services.ai.parser import GeminiIntentParser, IntentParser
from app1.services.tmdb.client import TMDBClient
from app1.services.watchlist.service import WatchlistService
from app1.storage.json_store import JsonStore
from app1.workflows.watchlist import WatchlistWorkflow


def get_store() -> JsonStore:
    return JsonStore()


def get_parser() -> IntentParser:
    return GeminiIntentParser()


def get_tmdb_client() -> TMDBClient:
    return TMDBClient()


def get_watchlist_service() -> WatchlistService:
    return WatchlistService(get_store())


def get_watchlist_workflow() -> WatchlistWorkflow:
    store = get_store()
    return WatchlistWorkflow(
        store=store,
        parser=get_parser(),
        tmdb_client=get_tmdb_client(),
        watchlist_service=WatchlistService(store),
    )
