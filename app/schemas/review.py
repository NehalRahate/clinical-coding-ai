from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ReviewCreate(BaseModel):
    """
    Schema used when a reviewer submits a review
    for an AI-generated prediction.
    """

    prediction_id: UUID
    reviewer_id: UUID

    action: str

    final_code_id: UUID | None = None
    comments: str | None = None


class ReviewResponse(BaseModel):
    """
    Schema returned by the API for a review.
    """

    id: UUID
    prediction_id: UUID | None = None
    reviewer_id: UUID | None = None

    action: str | None = None
    final_code_id: UUID | None = None
    comments: str | None = None

    reviewed_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)