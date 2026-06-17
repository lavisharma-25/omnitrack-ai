from langchain.tools import tool

from app.tools.excel_tools.utils import (
    get_tracker_service,
)


@tool
def create_tracker_tool(
    tracker_name: str,
    columns: list[str],
) -> str:
    """
    Create a new tracker.

    Args:
        tracker_name: Name of tracker.
        columns: Tracker columns.

    Returns:
        Success message.
    """

    service = get_tracker_service()

    return service.create_tracker(
        tracker_name=tracker_name,
        columns=columns,
    )