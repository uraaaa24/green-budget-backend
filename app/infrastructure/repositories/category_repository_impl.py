from sqlalchemy import UUID, or_
from sqlalchemy.orm import Session
from app.domain.category import Category
from app.domain.repositories.category_repository import CategoryRepository
from app.infrastructure.db.models.category import CategoryModel


class CategoryRepositoryImpl(CategoryRepository):
    def __init__(self, db: Session):
        self.db = db

    def find_all(self) -> list[Category]:
        categories = (
            self.db.query(CategoryModel)
            # usersのapiが完成次第コメントアウトを外す
            # .filter(
            #     or_(CategoryModel.user_id == user_id, CategoryModel.user_id == None)
            # )
            .all()
        )

        return [
            Category(
                id=c.id,
                name=c.name,
                description=c.description,
                transaction_type=c.transaction_type,
                created_at=c.created_at,
                updated_at=c.updated_at,
            )
            for c in categories
        ]

    def insert(self, category: Category) -> Category:
        db_category = CategoryModel(
            name=category.name,
            user_id=category.user_id,
            transaction_type=category.transaction_type,
            description=category.description,
        )
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)

        category.id = db_category.id
        return category
