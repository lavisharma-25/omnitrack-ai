from typing import Annotated, Optional
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

class TrackState(BaseModel):
    question: str
    refined_question: str | None = None
    answer: Optional[str] = None

    messages: Annotated[list[BaseMessage], add_messages] = Field(default_factory=list)