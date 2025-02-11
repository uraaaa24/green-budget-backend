from typing import Union
import jwt
from fastapi import Depends, HTTPException, status
from jwt.exceptions import InvalidTokenError, ExpiredSignatureError
from fastapi.security import (
    HTTPBearer,
)
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.config import settings
from app.domain.models.user import User
from app.infrastructure.db.deps import get_db
from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl
from app.schemas.user import UserCreate

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class TokenData(BaseModel):
    name: Union[str, None] = None
    email: str
    image: Union[str, None] = None


def get_user(db: Session, email: str):
    users_repository = UserRepositoryImpl(db)
    return users_repository.find_by_email(email)


def create_user(db: Session, user_create: UserCreate) -> User:
    users_repository = UserRepositoryImpl(db)
    user = User.create(
        display_name=user_create.display_name,
        email=user_create.email,
        image=user_create.image,
    )
    return users_repository.insert(user)


async def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(HTTPBearer()),
) -> User:
    try:
        payload = jwt.decode(
            token.credentials, settings.secret_key, algorithms=[ALGORITHM]
        )

        user_email: str = payload.get("email")
        user_name: str = payload.get("name")
        user_image: str = payload.get("image")

        if user_email is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        token_data = TokenData(email=user_email, name=user_name, image=user_image)
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
    user = get_user(db, email=token_data.email)
    if user is None:
        user_create = UserCreate(
            email=token_data.email,
            display_name=token_data.name,
            image=token_data.image,
        )
        user = create_user(db, user_create)
    return user
