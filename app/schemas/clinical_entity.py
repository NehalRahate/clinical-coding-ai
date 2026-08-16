from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class ClinicalEntityCreate(BaseModel):
    """
    Schema used when creating a clinical entity.
    """

    document_id: UUID
    entity_type: str | None = None
    entity_text: str | None = None
    start_position: int | None = None
    end_position: int | None = None
    confidence: float | None = None


class ClinicalEntityResponse(BaseModel):
    """
    Schema returned by the API for a clinical entity.
    """

    id: UUID
    document_id: UUID | None = None
    entity_type: str | None = None
    entity_text: str | None = None
    start_position: int | None = None
    end_position: int | None = None
    confidence: float | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)