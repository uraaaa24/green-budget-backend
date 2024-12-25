from decimal import Decimal
from typing import Literal, Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    user_id: UUID
    category_id: int
    amount: Decimal = Field(
        ..., gt=0, description="Transaction amount must be greater than zero"
    )
    transaction_type: Literal["income", "expense"]
    date: datetime
    note: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)


class TransactionResponse(TransactionCreate):
    id: int
