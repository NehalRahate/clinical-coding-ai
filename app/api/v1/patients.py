from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import Patient
from app.schemas import PatientCreate, PatientResponse


router = APIRouter(
    prefix="/patients",
    tags=["Patients"],
)


@router.post(
    "",
    response_model=PatientResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_patient(
    patient_data: PatientCreate,
    db: Session = Depends(get_db),
):
    """
    Create a new patient.
    """

    # Check whether external_id already exists
    existing_patient = db.execute(
        select(Patient).where(
            Patient.external_id == patient_data.external_id
        )
    ).scalar_one_or_none()

    if existing_patient:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Patient with this external_id already exists.",
        )

    # Create SQLAlchemy model
    patient = Patient(
        external_id=patient_data.external_id,
    )

    # Save to database
    db.add(patient)
    db.commit()

    # Refresh to get database-generated values
    db.refresh(patient)

    return patient


@router.get(
    "/{patient_id}",
    response_model=PatientResponse,
)
def get_patient(
    patient_id: UUID,
    db: Session = Depends(get_db),
):
    """
    Get a patient by UUID.
    """

    patient = db.execute(
        select(Patient).where(
            Patient.id == patient_id
        )
    ).scalar_one_or_none()

    if patient is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Patient not found.",
        )

    return patient