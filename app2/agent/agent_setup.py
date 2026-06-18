from langchain.agents import create_agent

from app.agent.prompts import SYSTEM_PROMPT
from app.agent.tools import load_tools
from app.services.llm_service import llm_model_flash as llm


def build_agent():
    """
    Create TrackFlow AI Agent.
    """

    agent = create_agent(
        model=llm,
        tools=load_tools(),
        system_prompt=SYSTEM_PROMPT,
    )

    return agent