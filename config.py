# config.py
import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///instance/database.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    UPLOAD_FOLDER = "uploads"
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

config = Config()