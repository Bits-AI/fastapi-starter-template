from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD

# 1. Define the PostgreSQL Connection String
# Format: postgresql+psycopg://user:password@host:port/dbname
DATABASE_URL = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:5432/{DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(
    bind=engine, 
    autoflush=False, 
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
