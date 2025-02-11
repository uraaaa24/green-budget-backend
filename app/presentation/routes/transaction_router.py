from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.deps import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.usecases.transaction_usecase import TransactionUsecase


router = APIRouter(tags=["Transactions"])
prefix = "/transactions"


@router.post(prefix, response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    usecase = TransactionUsecase(db)
    return usecase.create_transaction(transaction)


@router.get(prefix, response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db), auth=Depends(get_current_user)):
    usecase = TransactionUsecase(db)
    return usecase.get_transactions()
