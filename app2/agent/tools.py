from app.tools.tool_registery import get_all_tools


def load_tools():
    """
    Load all registered agent tools.
    """
    return get_all_tools()