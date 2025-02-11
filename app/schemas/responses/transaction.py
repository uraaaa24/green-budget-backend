from typing import Literal, Optional
from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class Category(BaseModel):
    id: int
    name: str


class TransactionResponse(BaseModel):
    id: int
    user_id: UUID
    category: str
    amount: int
    transaction_type: Literal["income", "expense"]
    date: datetime
    note: Optional[str] = None
    created_at: datetime


class PostTransactionResponse(BaseModel):
    user_id: UUID
    category_id: int
    amount: int
    transaction_type: Literal["income", "expense"]
    date: datetime
    note: Optional[str] = None
    created_at: datetime
