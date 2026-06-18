from app.tools.excel_tools.create_tracker import create_tracker_tool
from app.tools.excel_tools.list_trackers import list_trackers_tool
from app.tools.excel_tools.add_record import add_record_tool
from app.tools.excel_tools.list_records import list_records_tool
from app.tools.excel_tools.update_record import update_record_tool
from app.tools.excel_tools.delete_record import delete_record_tool


def get_all_tools():
    """
    Register all tools available to TrackFlow AI.
    """

    return [
        create_tracker_tool,
        list_trackers_tool,
        add_record_tool,
        list_records_tool,
        update_record_tool,
        delete_record_tool,
    ]