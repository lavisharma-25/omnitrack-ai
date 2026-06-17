from langchain.tools import tool

from app.models.common import ToolResponse
from app.tools.excel_tools.utils import get_tracker_service


@tool
def list_records_tool(
    tracker_name: str,
    limit: int = 50,
    offset: int = 0,
) -> dict:
    """
    Retrieve records from a tracker with pagination.

    Args:
        tracker_name: Name of the tracker.
        limit: Maximum number of records.
        offset: Starting position.

    Returns:
        Paginated records.
    """

    service = get_tracker_service()

    records = service.list_records(
        tracker_name=tracker_name,
    )

    paginated_records = records[offset : offset + limit]

    return ToolResponse(
        success=True,
        message=f"Retrieved {len(paginated_records)} record(s).",
        data={
            "tracker_name": tracker_name,
            "total_records": len(records),
            "offset": offset,
            "limit": limit,
            "records": paginated_records,
        },
    ).model_dump()