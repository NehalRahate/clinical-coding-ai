import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class ClinicalEntity(Base):
    """
    SQLAlchemy model for the clinical_entities table.
    """

    __tablename__ = "clinical_entities"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    document_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("documents.id"),
        nullable=True,
    )

    entity_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    entity_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    start_position: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    end_position: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    document: Mapped["Document | None"] = relationship(
        "Document",
        back_populates="clinical_entities",
    )