from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def find_by_email(self, email):
        pass

    @abstractmethod
    def insert(self, user):
        pass
