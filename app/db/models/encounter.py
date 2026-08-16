import uuid
from datetime import date, datetime
from uuid import UUID

from sqlalchemy import Date, DateTime, ForeignKey, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Encounter(Base):
    """
    SQLAlchemy model for the encounters table.
    """

    __tablename__ = "encounters"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    patient_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("patients.id"),
        nullable=True,
    )

    encounter_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    encounter_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    patient: Mapped["Patient | None"] = relationship(
        "Patient",
        back_populates="encounters",
    )
    documents: Mapped[list["Document"]] = relationship(
    "Document",
    back_populates="encounter",
)
