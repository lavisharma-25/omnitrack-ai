from langchain.agents import create_agent

from src.prompts import TRACKER_AGENT_PROMPT
from src.services.llm_service import llm_model_flash as llm
from src.tools.tracker_tools.create_tracker import create_tracker
from src.tools.tracker_tools.list_trackers import list_trackers
from src.tools.tracker_tools.edit_tracker import edit_tracker
from src.tools.tracker_tools.delete_tracker import delete_tracker
from src.tools.tracker_tools.remove_records import remove_records


def build_tracker_agent():

    return create_agent(
        model=llm,
        system_prompt=TRACKER_AGENT_PROMPT,
        tools=[
            create_tracker,
            list_trackers,
            edit_tracker,
            delete_tracker,
            remove_records
        ]
    )


tracker_agent = build_tracker_agent()