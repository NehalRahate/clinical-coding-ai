from collections.abc import Generator
from sqlalchemy.orm import Session
from app.db.database import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Provide a database session for a request.

    The session is closed automatically after the request
    has finished.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()