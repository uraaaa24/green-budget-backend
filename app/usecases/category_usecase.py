from app.domain.models.transaction import Category
from app.infrastructure.repositories.category_repository_impl import (
    CategoryRepositoryImpl,
)
from app.schemas.category import CategoryCreate


class CategoryUsecase:
    def __init__(self, db):
        self.repository = CategoryRepositoryImpl(db)

    def get_categories(self):
        return self.repository.find_all()

    def create_category(self, category_data=CategoryCreate):
        category = Category.create(
            name=category_data.name,
            user_id=category_data.user_id,
            transaction_type=category_data.transaction_type,
            description=category_data.description,
            created_at=category_data.created_at,
            updated_at=category_data.updated_at,
        )
        return self.repository.insert(category)
