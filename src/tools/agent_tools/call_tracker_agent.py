from langchain_core.messages import HumanMessage

from src.agents.tracker_management.agent import tracker_agent


def call_tracker_agent(query: str):
    """
    Routes tracker-related user requests to Tracker Management Agent.

    This tool is used when the user wants to:
    - create a tracker
    - list trackers
    - edit tracker schema
    - delete a tracker
    - remove records

    Input:
        query (str): Natural language request from supervisor

    Output:
        Tracker agent response
    """
    return tracker_agent.invoke({
        "messages": [
            HumanMessage(content=query)
        ]
    })