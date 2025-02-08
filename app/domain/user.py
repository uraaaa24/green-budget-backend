from dataclasses import dataclass
from datetime import datetime

from pydantic import Field


@dataclass
class User:
    id: int
    display_name: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
