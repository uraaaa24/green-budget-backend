from typing import Literal, Optional
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class CategoryCreate(BaseModel):
    name: str
    description: str
    user_id: UUID
    transaction_type: Literal["income", "expense"]


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str
    user_id: Optional[UUID]
    transaction_type: Literal["income", "expense"]
    created_at: datetime
    updated_at: datetime
