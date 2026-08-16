import sys
from pathlib import Path

# Ensures project root is in sys.path regardless of execution directory
sys.path.append(str(Path(__file__).resolve().parent.parent))

from datetime import datetime, timezone
from uuid import uuid4
from pydantic import ValidationError

from app.schemas import (
    CodeCreate, CodeResponse,
    DocumentCreate, DocumentResponse,
    EncounterCreate, EncounterResponse,
    PatientCreate, PatientResponse,
    PredictionCreate, PredictionResponse,
    ReviewCreate, ReviewResponse,
    UserCreate, UserResponse,
)


def test_schemas():
    print("--- Testing Pydantic Schemas ---")

    # 1. User Schemas
    user_create = UserCreate(email="coder@example.com", password="securepassword123", role="CLINICAL_CODER")
    user_resp = UserResponse(
        id=uuid4(),
        email=user_create.email,
        role=user_create.role,
        created_at=datetime.now(timezone.utc),
    )
    print(f"✅ UserResponse valid: {user_resp.email} ({user_resp.role})")

    # Test invalid email validation
    try:
        UserCreate(email="invalid-email", password="123", role="ADMIN")
    except ValidationError:
        print("✅ UserCreate caught invalid email format correctly.")

    # 2. Patient Schemas (Using external_id)
    patient_create = PatientCreate(external_id="PAT-12345")
    patient_resp = PatientResponse(
        id=uuid4(),
        **patient_create.model_dump(),
        created_at=datetime.now(timezone.utc),
    )
    print(f"✅ PatientResponse valid: External ID {patient_resp.external_id}")

    # 3. Encounter Schemas
    encounter_create = EncounterCreate(patient_id=patient_resp.id, encounter_type="INPATIENT")
    encounter_resp = EncounterResponse(
        id=uuid4(),
        **encounter_create.model_dump(),
        created_at=datetime.now(timezone.utc),
    )
    print(f"✅ EncounterResponse valid: Type {encounter_resp.encounter_type}")

    # 4. Document Schemas
    doc_create = DocumentCreate(
    encounter_id=encounter_resp.id,
    file_name="patient_report.pdf",
    s3_key="documents/patient_report.pdf",
    )
    doc_resp = DocumentResponse(
    id=uuid4(),
    **doc_create.model_dump(),
    extracted_text="Patient presents with type 2 diabetes.",
    status="UPLOADED",
    created_at=datetime.now(timezone.utc),
    )
    print(f"✅ DocumentResponse valid: Doc ID {doc_resp.id}")

    # 5. Code Schemas
    code_create = CodeCreate(
        code_system="ICD-10-CM",
        code="E11.9",
        description="Type 2 diabetes mellitus without complications",
    )
    code_resp = CodeResponse(
        id=uuid4(),
        **code_create.model_dump(),
    )
    print(f"✅ CodeResponse valid: {code_resp.code_system} {code_resp.code}")

    # 6. Prediction Schemas
    pred_create = PredictionCreate(
        document_id=doc_resp.id,
        code_id=code_resp.id,
        confidence=0.95,
        rank=1,
        status="PENDING_REVIEW",
    )
    pred_resp = PredictionResponse(
        id=uuid4(),
        **pred_create.model_dump(),
        created_at=datetime.now(timezone.utc),
    )
    print(f"✅ PredictionResponse valid: Rank {pred_resp.rank} (Confidence: {pred_resp.confidence})")

    # 7. Review Schemas
    review_create = ReviewCreate(
        prediction_id=pred_resp.id,
        reviewer_id=user_resp.id,
        action="APPROVED",
        final_code_id=code_resp.id,
        comments="Clinically accurate.",
    )
    review_resp = ReviewResponse(
        id=uuid4(),
        **review_create.model_dump(),
        reviewed_at=datetime.now(timezone.utc),
    )
    print(f"✅ ReviewResponse valid: Action {review_resp.action}")

    print("\n🎉 All Pydantic schemas validated successfully!")


if __name__ == "__main__":
    test_schemas()