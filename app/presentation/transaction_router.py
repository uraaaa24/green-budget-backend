from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.transaction import Transaction
from app.infrastructure.db.base import SessionLocal
from app.infrastructure.db.deps import get_db
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.usecases.transaction_usecase import TransactionUsecase


router = APIRouter()


@router.post("/", response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    usecase = TransactionUsecase(db)
    return usecase.create_transaction(transaction)


@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    usecase = TransactionUsecase(db)
    return usecase.get_transactions()
