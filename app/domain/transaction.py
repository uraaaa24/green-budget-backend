from decimal import Decimal
from typing import Optional
from uuid import UUID
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


@dataclass
class Category:
    id: int
    name: str


@dataclass
class Transaction:
    user_id: UUID
    category: Category
    amount: int
    transaction_type: str
    date: datetime
    id: Optional[int] = None
    note: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    @classmethod
    def create(
        cls,
        user_id: UUID,
        category: Category,
        amount: int,
        transaction_type: str,
        date: datetime,
        note: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        return cls(
            user_id=user_id,
            category=category,
            amount=amount,
            transaction_type=transaction_type,
            date=date,
            note=note,
            created_at=created_at or datetime.now(),
        )
