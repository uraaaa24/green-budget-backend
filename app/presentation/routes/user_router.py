from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.models.user import User
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.deps import get_db
from app.infrastructure.db.models.user import UserModel
from app.usecases.user_usecase import UserUsecase


router = APIRouter(tags=["Users"])
prefix = "/users"


@router.get(f"{prefix}/me")
async def read_users_me(auth_user: UserModel = Depends(get_current_user)):
    return auth_user
