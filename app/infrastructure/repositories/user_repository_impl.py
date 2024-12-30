from sqlalchemy.orm import Session

from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.db.models.user import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_firebase_uid(self, firebase_uid) -> UserModel:
        user = (
            self.db.query(UserModel)
            .filter(UserModel.firebase_uid == firebase_uid)
            .first()
        )
        return user
