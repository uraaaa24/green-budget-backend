from app.infrastructure.repositories.user_repository_impl import UserRepositoryImpl


class UserUsecase:
    def __init__(self, db):
        self.repository = UserRepositoryImpl(db)

    def get_user(self, user_id: str):
        return self.repository.find_by_email(user_id)
