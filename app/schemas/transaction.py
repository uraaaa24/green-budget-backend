from typing import Literal, Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class TransactionCreate(BaseModel):
    user_id: UUID
    category_id: int
    amount: float
    transaction_type: Literal["income", "expense"]
    date: datetime
    description: Optional[str] = None


class TransactionResponse(TransactionCreate):
    id: int
