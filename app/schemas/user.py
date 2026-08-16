from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr


class UserCreate(BaseModel):
    """
    Schema used when creating a new user.
    """

    email: EmailStr
    password: str
    role: str


class UserResponse(BaseModel):
    """
    Schema returned by the API for a user.

    password_hash is intentionally excluded.
    """

    id: UUID
    email: EmailStr
    role: str
    created_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)