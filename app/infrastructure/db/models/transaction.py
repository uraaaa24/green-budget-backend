from enum import Enum

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func

from app.domain.transaction import TransactionType
from app.infrastructure.db.base import Base


class TransactionModel(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)
    date = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
