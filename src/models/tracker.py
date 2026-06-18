from pydantic import BaseModel, Field, field_validator
from typing import List, Literal


ColumnType = Literal["string", "int", "float", "bool", "date"]


class ColumnSchema(BaseModel):
    name: str = Field(..., min_length=1)
    type: ColumnType


class CreateTrackerRequest(BaseModel):
    name: str = Field(..., min_length=1)
    columns: List[ColumnSchema]

    @field_validator("columns")
    @classmethod
    def validate_columns(cls, v):
        if len(v) == 0:
            raise ValueError("At least one column is required")
        return v