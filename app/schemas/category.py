from typing import Literal
from uuid import UUID
from pydantic import BaseModel, Field
from datetime import datetime


class CategoryCreate(BaseModel):
    name: str
    description: str
    user_id: UUID
    transaction_type: Literal["income", "expense"]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class CategoryResponse(CategoryCreate):
    id: int
