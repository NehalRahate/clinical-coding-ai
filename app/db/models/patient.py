import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, String, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base


class Patient(Base):
    """
    SQLAlchemy model for the patients table.
    """

    __tablename__ = "patients"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    external_id: Mapped[str] = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    )
    encounters: Mapped[list["Encounter"]] = relationship(
        "Encounter",
        back_populates="patient",
    )    