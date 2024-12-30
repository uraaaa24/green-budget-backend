from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.domain.user import User
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.deps import get_db
from app.infrastructure.db.models.user import UserModel
from app.usecases.user_usecase import UserUsecase


router = APIRouter(tags=["Users"])
prefix = "/users"


@router.get(f"{prefix}/me")
async def read_users_me(db: Session = Depends(get_db), cred=Depends(get_current_user)):
    # return UserModel(
    #     firebase_uid=cred["uid"],
    #     email=cred["email"],
    #     display_name=cred["email"],
    # )
    usecase = UserUsecase(db)
    return usecase.get_user(cred["sub"])
