from sqlalchemy.orm import Session
from app.domain.models.transaction import PostTransaction, Transaction
from app.domain.repositories.transaction_repository import TransactionRepository
from app.infrastructure.db import TransactionModel
from app.infrastructure.db.models.category import CategoryModel


class TransactionRepositoryImpl(TransactionRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_all(self, user_id: str) -> list[Transaction]:
        transactions = (
            self.db.query(
                TransactionModel,
                CategoryModel.name.label("category_name"),
            )
            .outerjoin(CategoryModel, TransactionModel.category_id == CategoryModel.id)
            .filter(TransactionModel.user_id == user_id)
            .all()
        )

        return [
            Transaction(
                id=t.TransactionModel.id,
                category=t.category_name,
                amount=t.TransactionModel.amount,
                transaction_type=t.TransactionModel.transaction_type,
                date=t.TransactionModel.date,
                note=t.TransactionModel.note,
            )
            for t in transactions
        ]

    def insert(self, transaction: PostTransaction) -> PostTransaction:
        db_transaction = TransactionModel(
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

        transaction.id = db_transaction.id
        return transaction
