import uuid
from datetime import datetime
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String, Text, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base





class Review(Base):
    """
    SQLAlchemy model for the reviews table.

    Stores human review decisions for AI-generated
    ICD-10-CM and CPT predictions.
    """

    __tablename__ = "reviews"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    prediction_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("predictions.id"),
        nullable=True,
    )

    reviewer_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    action: Mapped[str | None] = mapped_column(
        String,
        nullable=True,
    )

    final_code_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("codes.id"),
        nullable=True,
    )

    comments: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    reviewed_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    prediction: Mapped["Prediction | None"] = relationship(
        "Prediction",
        back_populates="reviews",
    )

    reviewer: Mapped["User | None"] = relationship(
        "User",
        back_populates="reviews",
    )

    final_code: Mapped["Code | None"] = relationship(
        "Code",
        back_populates="reviews",
    )
    # user = relationship("User", back_populates="reviews")    
    reviewer: Mapped["User | None"] = relationship(
        "User",
        back_populates="reviews",
    )







    