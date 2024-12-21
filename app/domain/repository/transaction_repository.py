from abc import ABC, abstractmethod

from app.domain.transaction import Transaction


class TransactionRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Transaction]:
        pass

    @abstractmethod
    def insert(self, transaction: Transaction) -> Transaction:
        pass
