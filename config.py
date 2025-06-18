import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///instance/database.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # S3 Config
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_S3_BUCKET_NAME = os.getenv("AWS_S3_BUCKET_NAME")
    AWS_S3_REGION = os.getenv("AWS_S3_REGION", "")
    AWS_S3_BASE_URL = os.getenv("AWS_S3_BASE_URL")  # e.g., https://bucket.s3.region.amazonaws.com

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

config = Config()
