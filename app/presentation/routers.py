from fastapi import APIRouter

# from app.presentation.category_router import router as category_router
from app.presentation.transaction_router import router as transaction_router
from app.presentation.user_router import router as user_router

router = APIRouter(prefix="/api")

router.include_router(transaction_router)
router.include_router(user_router)
# router.include_router(category_router)
