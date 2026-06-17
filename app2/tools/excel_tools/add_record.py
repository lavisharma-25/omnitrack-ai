from typing import Any

from langchain.tools import tool

from app.models.common import ToolResponse
from app.tools.excel_tools.utils import get_tracker_service


@tool
def add_record_tool(
    tracker_name: str,
    data: dict[str, Any],
) -> dict:
    """
    Add a record to a tracker.
    """

    service = get_tracker_service()

    record_id = service.add_record(
        tracker_name=tracker_name,
        data=data,
    )

    return ToolResponse(
        success=True,
        message="Record added successfully.",
        data={
            "record_id": record_id,
            "tracker_name": tracker_name,
        },
    ).model_dump()