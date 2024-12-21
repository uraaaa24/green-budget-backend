from sqlalchemy.orm import Session
from app.infrastructure.db.base import SessionLocal


def get_db():
    """Database session dependency."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
