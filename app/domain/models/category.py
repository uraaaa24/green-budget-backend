from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID


@dataclass
class Category:
    name: str
    transaction_type: str
    id: Optional[int] = None
    user_id: Optional[UUID] = None
    description: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    @property
    def is_default(self) -> bool:
        return self.user_id is None

    @classmethod
    def create(
        cls,
        user_id: UUID,
        transaction_type: str,
        name: str,
        description: Optional[str] = None,
    ):
        now = datetime.now()
        return cls(
            id=None,
            user_id=user_id,
            transaction_type=transaction_type,
            name=name,
            description=description,
            created_at=now,
            updated_at=now,
        )
