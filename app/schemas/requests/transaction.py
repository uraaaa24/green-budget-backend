from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import Literal, Optional


class CreateTransaction(BaseModel):
    amount: int
    transaction_type: Literal["income", "expense"]
    date: datetime
    category_id: Optional[int] = None
    note: Optional[str] = None
