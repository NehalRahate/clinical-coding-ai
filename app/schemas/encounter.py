from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EncounterCreate(BaseModel):
    """
    Schema used when creating a new clinical encounter.
    """

    patient_id: UUID
    encounter_type: str | None = None
    encounter_date: date | None = None


class EncounterResponse(BaseModel):
    """
    Schema returned by the API for an encounter.
    """

    id: UUID
    patient_id: UUID | None = None
    encounter_type: str | None = None
    encounter_date: date | None = None
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)