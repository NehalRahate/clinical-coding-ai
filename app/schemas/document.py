from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    """
    Schema used when creating a document record.
    """

    encounter_id: UUID | None = None
    file_name: str | None = None
    s3_key: str | None = None


class DocumentResponse(BaseModel):
    """
    Schema returned by the API for a document.
    """

    id: UUID
    encounter_id: UUID | None = None
    file_name: str | None = None
    s3_key: str | None = None
    extracted_text: str | None = None
    status: str | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)