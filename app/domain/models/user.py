from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from pydantic import Field


@dataclass
class User:
    id: UUID
    display_name: str
    email: str
    image: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @classmethod
    def create(cls, display_name: str, email: str, image: str):
        return cls(
            id=UUID(int=0),
            display_name=display_name,
            email=email,
            image=image,
        )
