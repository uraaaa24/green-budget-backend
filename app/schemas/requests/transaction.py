from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional


class CreateTransaction(BaseModel):
    user_id: UUID
    category_id: int
    amount: int
    transaction_type: Literal["income", "expense"]
    date: datetime
    note: Optional[str] = None
