from fastapi import APIRouter
from app.presentation.transaction_router import router as transaction_router

router = APIRouter()

router.include_router(
    transaction_router, prefix="/api/transactions", tags=["Transactions"]
)
