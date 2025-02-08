from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str):
        pass
