import uuid
from uuid import UUID

from sqlalchemy import Boolean, String, Text, UniqueConstraint, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base
from app.db.models.prediction import Prediction
from app.db.models.review import Review


class Code(Base):
    """
    SQLAlchemy model for the codes table.

    Stores ICD-10-CM, CPT, and potentially other
    clinical coding systems.
    """

    __tablename__ = "codes"

    __table_args__ = (
        UniqueConstraint(
            "code_system",
            "code",
            name="codes_code_system_code_key",
        ),
    )

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
    )

    code_system: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    code: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    active: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True,
        server_default=text("true"),
    )
    predictions: Mapped[list["Prediction"]] = relationship(
    "Prediction",
    back_populates="code",
    )
    reviews: Mapped[list["Review"]] = relationship(
        "Review",
        back_populates="final_code",
    )