from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class PredictionCreate(BaseModel):
    """
    Schema used when creating an AI-generated prediction.
    """

    document_id: UUID
    code_id: UUID

    model_version: str | None = None

    confidence: float | None = Field(
        default=None,
        ge=0.0,
        le=1.0,
    )

    rank: int | None = Field(
        default=None,
        ge=1,
    )

    evidence: str | None = None
    status: str | None = None


class PredictionResponse(BaseModel):
    """
    Schema returned by the API for an AI prediction.
    """

    id: UUID
    document_id: UUID | None = None
    code_id: UUID | None = None

    model_version: str | None = None
    confidence: float | None = None
    rank: int | None = None
    evidence: str | None = None
    status: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)