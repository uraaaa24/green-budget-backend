from app.domain.transaction import Transaction
from app.infrastructure.repositories.transaction_repository_impl import (
    TransactionRepositoryImpl,
)
from app.schemas.transaction import TransactionCreate


class TransactionUsecase:
    def __init__(self, db):
        self.repository = TransactionRepositoryImpl(db)

    def create_transaction(self, transaction_data=TransactionCreate):
        transaction = Transaction.create(
            user_id=transaction_data.user_id,
            category_id=transaction_data.category_id,
            amount=transaction_data.amount,
            transaction_type=transaction_data.transaction_type,
            date=transaction_data.date,
            note=transaction_data.note,
        )
        return self.repository.insert(transaction)

    def get_transactions(self):
        return self.repository.find_all()
