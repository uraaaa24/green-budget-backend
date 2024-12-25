from decimal import Decimal
from typing import Optional
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class TransactionId:
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise ValueError("Transaction ID must be a positive integer")


@dataclass
class TransactionAmount:
    value: Decimal

    def __post_init__(self):
        if self.value == 0:
            raise ValueError("Transaction amount must be a non-zero value")


@dataclass
class Transaction:
    user_id: UUID
    category_id: int
    amount: TransactionAmount
    transaction_type: TransactionType
    date: datetime
    id: Optional[TransactionId] = None
    note: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        user_id: UUID,
        category_id: int,
        amount: Decimal,
        transaction_type: str,
        date: datetime,
        note: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        return cls(
            user_id=user_id,
            category_id=category_id,
            amount=TransactionAmount(amount),
            transaction_type=TransactionType(transaction_type),
            date=date,
            note=note,
            created_at=created_at or datetime.now(),
        )
