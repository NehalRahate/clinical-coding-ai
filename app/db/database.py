from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


# -------------------------------------------------------------------
# Database Configuration
# -------------------------------------------------------------------

DATABASE_URL = "postgresql+psycopg2://postgres:2233@localhost:5432/clinical_coding_ai"

# -------------------------------------------------------------------
# Database Engine
# -------------------------------------------------------------------

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)


# -------------------------------------------------------------------
# Database Session
# -------------------------------------------------------------------

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# -------------------------------------------------------------------
# Base Model
# -------------------------------------------------------------------

class Base(DeclarativeBase):
    """
    Base class for all SQLAlchemy models.
    """
    pass