from sqlalchemy.orm import Session

from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.db.models.user import UserModel


class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_by_user_id(self, user_id) -> UserModel:
        user = self.db.query(UserModel).filter(UserModel.user_id == user_id).first()
        return user
