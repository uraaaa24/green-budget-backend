from abc import ABC, abstractmethod

from app.domain.category import Category


class CategoryRepository(ABC):
    @abstractmethod
    def find_all(self) -> list[Category]:
        pass

    @abstractmethod
    def insert(self, category: Category) -> Category:
        pass
