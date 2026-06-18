import pandas as pd
from src.tools.tracker_tools._shared import get_tracker_path


def remove_records(name: str, condition: dict = None):
    """
    Remove records from a tracker.

    Args:
        name (str): Tracker name
        condition (dict, optional): Filter condition

    Returns:
        dict: Result of deletion
    """

    path = get_tracker_path(name)

    if not path.exists():
        return {"error": "Tracker not found"}

    df = pd.read_excel(path)

    if condition is None:
        df = df.iloc[0:0]  # clear all
    else:
        col = condition["column"]
        op = condition["operator"]
        value = condition["value"]

        if op == ">":
            df = df[df[col] <= value]
        elif op == "<":
            df = df[df[col] >= value]
        elif op == "==":
            df = df[df[col] != value]
        else:
            return {"error": "Unsupported operator"}

    df.to_excel(path, index=False)

    return {
        "status": "success",
        "message": "Records removed successfully"
    }