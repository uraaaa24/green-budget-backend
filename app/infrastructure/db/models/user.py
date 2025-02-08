from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.infrastructure.db.base import Base
from sqlalchemy.dialects.postgresql import UUID


class UserModel(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    display_name = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    image = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
