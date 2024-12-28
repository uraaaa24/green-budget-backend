from fastapi import APIRouter, Depends

from app.domain.user import User
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.models.user import UserModel


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def read_users_me(cred=Depends(get_current_user)):
    # return UserModel(
    #     firebase_uid=cred["uid"],
    #     email=cred["email"],
    #     display_name=cred["email"],
    # )
    return cred
