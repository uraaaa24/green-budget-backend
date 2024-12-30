from fastapi import APIRouter, Depends

from app.domain.user import User
from app.infrastructure.auth.deps import get_current_user
from app.infrastructure.db.models.user import UserModel


router = APIRouter(tags=["Users"])
prefix = "/users"


@router.get(f"{prefix}/me")
async def read_users_me(cred=Depends(get_current_user)):
    # return UserModel(
    #     firebase_uid=cred["uid"],
    #     email=cred["email"],
    #     display_name=cred["email"],
    # )
    return cred
