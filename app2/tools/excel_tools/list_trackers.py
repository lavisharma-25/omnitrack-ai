from langchain.tools import tool

from app.models.common import ToolResponse
from app.tools.excel_tools.utils import get_tracker_service


@tool
def list_trackers_tool() -> dict:
    """
    Retrieve all available trackers.

    Returns:
        List of tracker names.
    """

    service = get_tracker_service()

    trackers = service.list_trackers()

    return ToolResponse(
        success=True,
        message=f"Found {len(trackers)} tracker(s).",
        data={
            "total_trackers": len(trackers),
            "trackers": trackers,
        },
    ).model_dump()