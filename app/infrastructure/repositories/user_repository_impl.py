import uuid
from sqlalchemy.orm import Session

from app.domain.repositories.user_repository import UserRepository
from app.domain.user import User
from app.infrastructure.db.models.user import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email) -> UserModel:
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        return user

    def insert(self, user: User) -> User:
        db_user = UserModel(
            id=str(uuid.uuid4()),
            display_name=user.display_name,
            email=user.email,
            image=user.image,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        user.id = db_user.id
        return user
