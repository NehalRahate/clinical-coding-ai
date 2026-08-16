from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CodeCreate(BaseModel):
    """
    Schema used when creating a clinical code.
    """

    code_system: str
    code: str
    description: str
    active: bool = True


class CodeResponse(BaseModel):
    """
    Schema returned by the API for a clinical code.
    """

    id: UUID
    code_system: str
    code: str
    description: str
    active: bool | None = None

    model_config = ConfigDict(from_attributes=True)