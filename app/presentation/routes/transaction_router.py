from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.deps import get_db
from app.schemas.requests.transaction import CreateTransaction
from app.schemas.responses.transaction import TransactionResponse
from app.usecases.transaction_usecase import TransactionUsecase


router = APIRouter(tags=["Transactions"])
prefix = "/transactions"


@router.post(prefix, response_model=CreateTransaction)
def create_transaction(
    transaction: CreateTransaction,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    usecase = TransactionUsecase(db)
    return usecase.create_transaction(
        current_user.id,
        transaction,
    )


@router.get(prefix, response_model=list[TransactionResponse])
def get_transactions(
    db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    usecase = TransactionUsecase(db)
    return usecase.get_transactions(current_user.id)
