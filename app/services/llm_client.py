from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

from app.config import location, credentials, gemini_model_flash, gemini_model_lite


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

safety_settings = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE
}


# -----------------------------------------------------------------------------
# LLM Factory
# -----------------------------------------------------------------------------
def create_llm(model_name: str):
    return ChatGoogleGenerativeAI(
        model=model_name,
        safety_settings=safety_settings,
        **config,
    )


# -----------------------------------------------------------------------------
# Models
# -----------------------------------------------------------------------------
llm_model_flash = create_llm(gemini_model_flash)

llm_model_lite = create_llm(gemini_model_lite)
