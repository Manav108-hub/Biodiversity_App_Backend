import os
import boto3
import uuid
from fastapi import UploadFile
import requests
from config import config

# Initialize S3 client
s3 = boto3.client(
    "s3",
    region_name=config.AWS_S3_REGION,
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
)

def save_uploaded_file(file: UploadFile) -> str:
    # Generate a unique filename
    ext = file.filename.rsplit(".", 1)[-1]
    key = f"{uuid.uuid4().hex}.{ext}"
    
    # Upload to S3
    s3.upload_fileobj(
        file.file,
        config.AWS_S3_BUCKET_NAME,
        key,
        # ExtraArgs={"ACL": "public-read", "ContentType": file.content_type}
    )
    
    # Return public URL
    return f"{config.AWS_S3_BASE_URL}/{key}"

def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in config.ALLOWED_EXTENSIONS

def validate_email(email: str) -> bool:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_region_name(lat, lng):
    try:
        api_key = os.getenv("OPENCAGE_KEY")
        if not api_key:
            print("Missing OPENCAGE_KEY")
            return "Unknown"

        url = f"https://api.opencagedata.com/geocode/v1/json?q={lat}+{lng}&key={api_key}"
        res = requests.get(url)
        data = res.json()

        if data and data.get("results"):
            components = data["results"][0]["components"]
            return components.get("country") or components.get("state") or "Unknown"
        return "Unknown"
    except Exception as e:
        print("Geocoding error:", e)
        return "Unknown"
