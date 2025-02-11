from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from uuid import UUID
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass(frozen=True)
class Category:
    id: int
    name: str


@dataclass
class Transaction:
    user_id: UUID
    category: str
    amount: int
    transaction_type: TransactionType
    date: datetime
    id: Optional[int] = None
    note: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class PostTransaction:
    user_id: UUID
    category_id: int
    amount: Decimal
    transaction_type: TransactionType
    date: datetime
    note: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
