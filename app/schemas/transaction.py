from typing import Literal
from psycopg2 import Date
from pydantic import BaseModel


class TransactionCreate(BaseModel):
    user_id: str
    category_id: str
    amount: float
    transaction_type: Literal["income", "expense"]
    date: Date
    description: str


class TransactionResponse(TransactionCreate):
    id: str
