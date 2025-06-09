from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.schema import Base
from config import Config
import os

# Add connect_args={"check_same_thread": False} ONLY for SQLite
if Config.DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        Config.DATABASE_URL, 
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(Config.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
