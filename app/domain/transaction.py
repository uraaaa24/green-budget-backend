from dataclasses import dataclass
from enum import Enum

from psycopg2 import Date


@dataclass
class TransactionId:
    value: str


@dataclass
class TransactionAmount:
    value: float

    def __post_init__(self):
        if self.value == 0:
            raise ValueError("Transaction amount must be a non-zero value")


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


@dataclass
class Transaction:
    id: TransactionId
    user_id: str
    category_id: str
    amount: TransactionAmount
    transaction_type: TransactionType
    date: Date
    description: str

    @classmethod
    def create(
        user_id: str,
        category_id: str,
        amount: TransactionAmount,
        transaction_type: TransactionType,
        date: Date,
        description: str,
    ):
        import uuid

        transaction_id = TransactionId(str(uuid.uuid4()))
        return Transaction(
            id=transaction_id,
            user_id=user_id,
            category_id=category_id,
            amount=amount,
            transaction_type=transaction_type,
            date=date,
            description=description,
        )
