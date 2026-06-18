from app.services.tracker_service import TrackerService


_tracker_service = TrackerService()


def get_tracker_service() -> TrackerService:
    """
    Singleton tracker service instance.
    """

    return _tracker_service