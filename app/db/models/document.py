import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base
from app.db.models.clinical_entity import ClinicalEntity


class Document(Base):
    """
    SQLAlchemy model for the documents table.
    """

    __tablename__ = "documents"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    encounter_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("encounters.id"),
        nullable=True,
    )

    file_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    s3_key: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    extracted_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    encounter: Mapped["Encounter | None"] = relationship(
        "Encounter",
        back_populates="documents",
    )
    clinical_entities: Mapped[list["ClinicalEntity"]] = relationship(
    "ClinicalEntity",
    back_populates="document",
)
    predictions: Mapped[list["Prediction"]] = relationship(
    "Prediction",
    back_populates="document",
)