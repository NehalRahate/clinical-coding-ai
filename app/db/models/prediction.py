import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import (
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Prediction(Base):
    """
    SQLAlchemy model for the predictions table.

    Stores ICD-10-CM and CPT predictions generated
    by the clinical coding AI models.
    """

    __tablename__ = "predictions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    document_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("documents.id"),
        nullable=True,
    )

    code_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("codes.id"),
        nullable=True,
    )

    model_version: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    confidence: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    rank: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    evidence: Mapped[str | None] = mapped_column(
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

    document: Mapped["Document | None"] = relationship(
        "Document",
        back_populates="predictions",
    )

    code: Mapped["Code | None"] = relationship(
        "Code",
        back_populates="predictions",
    )
    reviews: Mapped[list["Review"]] = relationship(
    "Review",
    back_populates="prediction",
)