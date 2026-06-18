from langchain.tools import tool

from app.models.common import ToolResponse
from app.tools.excel_tools.utils import get_tracker_service


@tool
def delete_record_tool(
    tracker_name: str,
    record_id: str,
) -> dict:
    """
    Delete a record from a tracker.

    Args:
        tracker_name: Name of the tracker.
        record_id: UUID of the record to delete.

    Example:
        tracker_name="tasks"
        record_id="a7d1e9c0-2f47-4c84-9b92-bfae0e4aaf35"

    Returns:
        Deletion status.
    """

    service = get_tracker_service()

    message = service.delete_record(
        tracker_name=tracker_name,
        record_id=record_id,
    )

    return ToolResponse(
        success=True,
        message=message,
        data={
            "tracker_name": tracker_name,
            "record_id": record_id,
        },
    ).model_dump()