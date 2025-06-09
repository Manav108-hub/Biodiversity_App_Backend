# utils/helpers.py
from fastapi import UploadFile
from datetime import datetime
import uuid
from config import Config
import os

def save_uploaded_file(file: UploadFile):
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)
    
    filename = f"{uuid.uuid4()}_{file.filename}"
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    
    return filename

def allowed_file(filename: str):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def validate_email(email: str):
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None