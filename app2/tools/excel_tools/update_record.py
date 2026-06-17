from typing import Any

from langchain.tools import tool

from app.models.common import ToolResponse
from app.tools.excel_tools.utils import get_tracker_service


@tool
def update_record_tool(
    tracker_name: str,
    record_id: str,
    updates: dict[str, Any],
) -> dict:
    """
    Update an existing record in a tracker.

    Args:
        tracker_name: Name of the tracker.
        record_id: UUID of the record to update.
        updates: Fields to update.

    Example:
        tracker_name="tasks"
        record_id="a7d1e9c0-2f47-4c84-9b92-bfae0e4aaf35"
        updates={
            "status": "Completed",
            "priority": "Low"
        }

    Returns:
        Update status.
    """

    service = get_tracker_service()

    message = service.update_record(
        tracker_name=tracker_name,
        record_id=record_id,
        updates=updates,
    )

    return ToolResponse(
        success=True,
        message=message,
        data={
            "tracker_name": tracker_name,
            "record_id": record_id,
            "updated_fields": list(updates.keys()),
        },
    ).model_dump()