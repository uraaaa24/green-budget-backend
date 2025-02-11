from abc import ABC, abstractmethod

from app.domain.models.transaction import PostTransaction, Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Transaction]:
        pass

    @abstractmethod
    def insert(self, transaction: PostTransaction) -> Transaction:
        pass
