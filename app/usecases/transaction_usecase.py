from app.domain.models.transaction import PostTransaction
from app.infrastructure.repositories.transaction_repository_impl import (
    TransactionRepositoryImpl,
)
from app.schemas.requests.transaction import CreateTransaction


class TransactionUsecase:
    def __init__(self, db):
        self.repository = TransactionRepositoryImpl(db)

    def create_transaction(self, user_id: str, transaction_data=CreateTransaction):
        transaction = PostTransaction(
            user_id=user_id,
            category_id=transaction_data.category_id,
            amount=transaction_data.amount,
            transaction_type=transaction_data.transaction_type,
            date=transaction_data.date,
            note=transaction_data.note,
        )
        return self.repository.insert(transaction)

    def get_transactions(self, user_id: str):
        return self.repository.find_all(user_id)
