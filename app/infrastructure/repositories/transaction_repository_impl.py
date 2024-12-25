from sqlalchemy.orm import Session
from app.domain.repositories.transaction_repository import TransactionRepository
from app.domain.transaction import Transaction, TransactionId
from app.infrastructure.db import TransactionModel


class TransactionRepositoryImpl(TransactionRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_all(self) -> list[Transaction]:
        transactions = self.db.query(TransactionModel).all()
        return [
            Transaction(
                id=t.id,
                user_id=t.user_id,
                category_id=t.category_id,
                amount=t.amount,
                transaction_type=t.transaction_type,
                date=t.date,
                note=t.note,
            )
            for t in transactions
        ]

    def insert(self, transaction: Transaction) -> Transaction:
        db_transaction = TransactionModel(
            id=transaction.id.value,
            user_id=transaction.user_id,
            category_id=transaction.category_id,
            amount=transaction.amount,
            transaction_type=transaction.transaction_type,
            date=transaction.date,
            note=transaction.note,
        )
        self.db.add(db_transaction)
        self.db.commit()
        self.db.refresh(db_transaction)

        transaction.id = TransactionId(value=db_transaction.id)
        return transaction
