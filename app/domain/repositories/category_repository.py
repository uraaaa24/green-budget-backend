from abc import ABC, abstractmethod

from app.domain.models.transaction import Category


class CategoryRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Category]:
        pass

    @abstractmethod
    def insert(self, category: Category) -> Category:
        pass
