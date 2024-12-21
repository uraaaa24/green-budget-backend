from dataclasses import dataclass
from datetime import datetime
import random


@dataclass
class TransactionId:
    value: int


@dataclass
class TransactionAmount:
    value: float

    def __post_init__(self):
        if self.value == 0:
            raise ValueError("Transaction amount must be a non-zero value")


@dataclass
class Transaction:
    id: TransactionId
    user_id: int
    category_id: int
    amount: TransactionAmount
    transaction_type: str
    date: datetime
    description: str

    @classmethod
    def create(
        cls,
        user_id: int,
        category_id: int,
        amount: TransactionAmount,
        transaction_type: str,
        date: datetime,
        description: str,
    ):
        transaction_id = TransactionId(value=random.randint(1, 10**6))
        return Transaction(
            id=transaction_id,
            user_id=user_id,
            category_id=category_id,
            amount=amount,
            transaction_type=transaction_type,
            date=date,
            description=description,
        )
