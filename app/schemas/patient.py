from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class PatientCreate(BaseModel):
    """
    Schema used when creating a new patient.
    """
    # mrn: str  # <--- Ensure mrn is defined here
    # name: str    

    external_id: str


class PatientResponse(BaseModel):
    """
    Schema returned by the API when working with a patient.
    """

    id: UUID
    external_id: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)