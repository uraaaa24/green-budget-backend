from fastapi import APIRouter
from app.presentation.transaction_router import router as transaction_router

router = APIRouter(prefix="/api")

router.include_router(transaction_router, prefix="/transactions", tags=["Transactions"])
