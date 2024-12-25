from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from app.infrastructure.db.base import Base


class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    note = Column(String, nullable=True)
