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
    amount: int
    transaction_type: TransactionType
    date: datetime
    category: Optional[str] = None
    id: Optional[int] = None
    note: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)


@dataclass
class PostTransaction:
    user_id: UUID
    amount: Decimal
    transaction_type: TransactionType
    date: datetime
    category_id: Optional[int] = None
    note: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
