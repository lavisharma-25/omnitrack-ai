import json

from langchain_google_genai import ChatGoogleGenerativeAI
from app1.prompts.system_prompt import SYSTEM_PROMPT
from app1.config import location, credentials, gemini_model_flash, gemini_model_lite



# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
config = {
    "project": credentials.project_id,
    "credentials": credentials,
    "location": location,
    "vertexai": True,
    "temperature": 0,
    "model_kwargs": {
        "thinking": 0,
    },
}


# -----------------------------------------------------------------------------
# Initialize Gemini model
# -----------------------------------------------------------------------------
def create_llm(model_name: str):
    return ChatGoogleGenerativeAI(
        model=model_name,
        **config,
    )

llm_model_flash = create_llm(gemini_model_flash)
llm_model_lite = create_llm(gemini_model_lite)

class IntentParser:

    @staticmethod
    def parse(query: str):

        messages = [
            ("system", SYSTEM_PROMPT),
            ("human", query)
        ]

        response = llm_model_flash.invoke(messages)

        content = response.content

        return json.loads(content)