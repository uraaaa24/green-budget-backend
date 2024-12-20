from sqlalchemy import Column, Integer, String
from app.infrastructure.db.base import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firebase_uid = Column(String, nullable=False, unique=True, index=True)
    display_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
