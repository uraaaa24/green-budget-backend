from typing import Literal
from datetime import datetime
from pydantic import BaseModel


class TransactionCreate(BaseModel):
    user_id: int
    category_id: int
    amount: float
    transaction_type: Literal["income", "expense"]
    date: datetime
    description: str


class TransactionResponse(TransactionCreate):
    id: int
