from fastapi import APIRouter
from app.domain.transaction import Transaction
from app.infrastructure.db.base import SessionLocal
from app.schemas.transaction import TransactionCreate, TransactionResponse


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# TODO: スキーマを作成して、レスポンスモデル追加する
@router.post("/transaction", response_model=TransactionResponse)
def create_transaction(self, transaction_data=TransactionCreate):
    transaction = Transaction.create(
        user_id=transaction_data.user_id,
        category_id=transaction_data.category_id,
        amount=transaction_data.amount,
        transaction_type=transaction_data.transaction_type,
        date=transaction_data.date,
        description=transaction_data.description,
    )
    return self.transaction_repository.insert(transaction)
