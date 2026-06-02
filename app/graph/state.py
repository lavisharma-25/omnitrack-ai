from pydantic import BaseModel

class TrackState(BaseModel):
    question: str
    answer: str