from typing import Any

from pydantic import BaseModel, Field


class RecordCreate(BaseModel):
    """
    Dynamic record payload.
    """

    data: dict[str, Any] = Field(
        ...,
        description="Record data"
    )


class RecordUpdate(BaseModel):
    """
    Dynamic record update payload.
    """

    row_id: int = Field(
        ...,
        ge=1,
        description="Excel row number"
    )

    data: dict[str, Any]


class RecordDelete(BaseModel):
    """
    Record delete payload.
    """

    row_id: int = Field(
        ...,
        ge=1,
        description="Excel row number"
    )


class RecordResponse(BaseModel):
    """
    Single record response.
    """

    row_id: int
    data: dict[str, Any]


class RecordsResponse(BaseModel):
    """
    Multiple records response.
    """

    records: list[RecordResponse]