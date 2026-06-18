from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class TrackerCreate(BaseModel):
    """
    Request model for creating a tracker.
    """

    name: str = Field(
        ...,
        min_length=1,
        description="Tracker name",
    )

    columns: List[str] = Field(
        ...,
        min_length=1,
        description="Column names for tracker",
    )


class TrackerInfo(BaseModel):
    """
    Tracker metadata.
    """

    name: str
    columns: List[str]
    created_at: datetime | None = None


class TrackerListResponse(BaseModel):
    """
    Response model for listing trackers.
    """

    trackers: List[str]