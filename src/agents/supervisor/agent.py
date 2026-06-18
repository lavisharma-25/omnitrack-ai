from langchain.agents import create_agent

from src.prompts import SUPERVISOR_SYSTEM_PROMPT
from src.services.llm_service import llm_model_flash as llm
from src.tools.agent_tools.call_tracker_agent import call_tracker_agent



def build_supervisor_agent():
    supervisor_agent = create_agent(
            model=llm,
            tools=[call_tracker_agent],
            system_prompt=SUPERVISOR_SYSTEM_PROMPT
        )

    return supervisor_agent

supervisor_agent = build_supervisor_agent()