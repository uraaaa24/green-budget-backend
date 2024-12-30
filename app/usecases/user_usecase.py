from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


class UserUsecase:
    def __init__(self, db):
        self.repository = UserRepositoryImpl(db)

    def get_user(self, firebase_uid: str):
        return self.repository.find_by_firebase_uid(firebase_uid)
