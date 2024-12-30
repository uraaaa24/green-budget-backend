from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def find_by_firebase_uid(self, firebase_uid: str):
        pass
