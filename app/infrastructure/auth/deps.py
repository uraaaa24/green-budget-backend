from typing import Union
import jwt
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from fastapi.security import (
    HTTPBearer,
)
from pydantic import BaseModel
from app.core.config import settings

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# UserModelのフェイクデータベース
fake_users_db = {
    "test-example.com": {
        "id": "6f6d2f7e-3b4b-4e5c-8b6b-8c7c5d9c0f2a",
        "display_name": "John Doe",
        "email": "test-example.com",
        "created_at": "2021-01-01T00:00:00",
        "updated_at": "2021-01-01T00:00:00",
    }
}


class TokenData(BaseModel):
    username: Union[str, None] = None


def get_user(db, email: str):
    if email in db:
        user_dict = db[email]
        return {
            "id": user_dict["id"],
            "email": user_dict["email"],
            "display_name": user_dict["display_name"],
        }


async def get_current_user(token: str = Depends(HTTPBearer())):
    try:
        payload = jwt.decode(
            token.credentials, settings.secret_key, algorithms=[ALGORITHM]
        )
        user_email: str = payload.get("email")
        if user_email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = TokenData(username=user_email)
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token",
        )
    user = get_user(fake_users_db, email=token_data.username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
