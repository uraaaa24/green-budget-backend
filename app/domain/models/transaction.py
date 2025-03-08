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
    transaction_type: TransactionType
    description: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)


@dataclass
class Transaction:
    amount: int
    transaction_type: TransactionType
    date: datetime
    created_at: datetime = field(default_factory=datetime.now)
    category: Optional[str] = None
    id: Optional[int] = None
    note: Optional[str] = None


@dataclass
class PostTransaction:
    user_id: UUID
    amount: Decimal
    transaction_type: TransactionType
    date: datetime
    created_at: datetime = field(default_factory=datetime.now)
    category_id: Optional[int] = None
    note: Optional[str] = None
