from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from app.infrastructure.db.base import Base
from sqlalchemy.dialects.postgresql import UUID


class CategoryModel(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    transaction_type = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
