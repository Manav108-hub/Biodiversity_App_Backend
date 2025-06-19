import os
from typing import List, Optional

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from models.schema import User, Species, Question, SpeciesLog, Answer
from utils.database import get_db
from utils.auth import (
    create_access_token,
    get_current_user,
    admin_required
)
from utils.helpers import get_region_name, save_uploaded_file, validate_email
import json
from datetime import datetime
import pandas as pd
import io

router = APIRouter()

# Authentication routes
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    is_admin: bool = False

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(
    user: UserCreate,
    x_admin_secret: str = None,
    db: Session = Depends(get_db)
):
    if not validate_email(user.email):
        raise HTTPException(status_code=400, detail="Invalid email format")

    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")

    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")

    is_admin = False
    if user.is_admin:
        if x_admin_secret == os.getenv("ADMIN_SECRET"):
            is_admin = True
        else:
            raise HTTPException(status_code=403, detail="Invalid admin secret")

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
        is_admin=is_admin
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    access_token = create_access_token(data={"sub": str(db_user.id)})
    return {
        "message": "User registered successfully",
        "access_token": access_token,
        "user": db_user.to_dict()
    }

@router.post("/login")
async def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        (User.username == credentials.username) | (User.email == credentials.username)
    ).first()

    if not user or not user.check_password(credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": str(user.id)})
    return {
        "message": "Login successful",
        "access_token": access_token,
        "user": user.to_dict()
    }

# Species routes
@router.get("/species")
async def get_species(db: Session = Depends(get_db)):
    return {"species": [s.to_dict() for s in db.query(Species).all()]}

@router.post("/species")
async def create_species(
    name: str = Form(...),
    scientific_name: Optional[str] = Form(None),
    category: str = Form(...),
    description: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    db_species = Species(
        name=name,
        scientific_name=scientific_name,
        category=category,
        description=description
    )
    db.add(db_species)
    db.commit()
    db.refresh(db_species)
    return {
        "message": "Species created successfully",
        "species": db_species.to_dict()
    }

# Questions routes
class QuestionCreate(BaseModel):
    question_text: str
    question_type: str
    options: Optional[list] = None
    is_required: bool = True
    order_index: int = 0

@router.get("/questions")
async def get_questions(db: Session = Depends(get_db)):
    return {"questions": [q.to_dict() for q in db.query(Question).order_by(Question.order_index)]}

@router.post("/questions")
async def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return {
        "message": "Question created successfully",
        "question": db_question.to_dict()
    }

# Species logs routes
class AnswerCreate(BaseModel):
    question_id: int
    answer_text: str

class SpeciesLogCreate(BaseModel):
    species_id: int
    location_latitude: float | None = None
    location_longitude: float | None = None
    location_name: str | None = None
    notes: str | None = None
    answers: List[AnswerCreate] = []

@router.post("/species-logs")
async def create_species_log(
    species_log: str = Form(...),
    photo: UploadFile | None = File(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        data = json.loads(species_log)
        species_log_data = SpeciesLogCreate(**data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON in species_log: {e}")

    photo_path = None
    if photo:
        photo_path = save_uploaded_file(photo)

    db_log = SpeciesLog(
        user_id=current_user.id,
        species_id=species_log_data.species_id,
        location_latitude=species_log_data.location_latitude,
        location_longitude=species_log_data.location_longitude,
        location_name=species_log_data.location_name,
        notes=species_log_data.notes,
        photo_path=photo_path
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    for answer in species_log_data.answers:
        db_answer = Answer(
            species_log_id=db_log.id,
            question_id=answer.question_id,
            answer_text=answer.answer_text
        )
        db.add(db_answer)

    db.commit()
    return {
        "message": "Species log created successfully",
        "species_log": db_log.to_dict()
    }

@router.get("/species-logs")
async def get_user_species_logs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    logs = db.query(SpeciesLog).filter(SpeciesLog.user_id == current_user.id).all()
    return {"species_logs": [log.to_dict() for log in logs], "total_count": len(logs)}

@router.get("/species-logs/{log_id}")
async def get_species_log_detail(log_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    log = db.query(SpeciesLog).filter(SpeciesLog.id == log_id, SpeciesLog.user_id == current_user.id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Species log not found")
    return {"species_log": log.to_dict()}

# Admin routes
@router.get("/admin/users")
async def get_all_users(db: Session = Depends(get_db), admin: bool = Depends(admin_required)):
    return {"users": [user.to_dict() for user in db.query(User).all()]}

@router.get("/admin/all-logs")
async def get_all_species_logs(db: Session = Depends(get_db), admin: bool = Depends(admin_required)):
    logs = db.query(SpeciesLog).order_by(SpeciesLog.created_at.desc()).all()
    return {"species_logs": [log.to_dict() for log in logs], "total_count": len(logs)}

@router.get("/admin/export-csv")
async def export_csv(db: Session = Depends(get_db), admin: bool = Depends(admin_required)):
    logs = db.query(SpeciesLog).all()
    csv_data = []

    for log in logs:
        base_row = {
            "log_id": log.id,
            "username": log.user.username if log.user else "Unknown",
            "user_email": log.user.email if log.user else "N/A",
            "species_id": log.species_id,
            "species_name": log.species.name if log.species else "Unknown",
            "scientific_name": log.species.scientific_name if log.species else "N/A",
            "category": log.species.category if log.species else "N/A",
            "location_latitude": log.location_latitude,
            "location_longitude": log.location_longitude,
            "location_name": log.location_name,
            "notes": log.notes,
            "created_at": log.created_at.isoformat() if log.created_at else "N/A",
            "photo_url": log.photo_path or ""
        }

        for answer in log.answers:
            question_key = f"Q{answer.question_id}_{answer.question.question_text[:30]}" if answer.question else f"Q{answer.question_id}"
            base_row[question_key] = answer.answer_text

        csv_data.append(base_row)

    df = pd.DataFrame(csv_data)
    output = io.StringIO()
    df.to_csv(output, index=False)
    output.seek(0)

    return StreamingResponse(
        io.BytesIO(output.getvalue().encode()),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=biodiversity_export.csv"}
    )

# Utility routes
@router.get("/profile")
async def get_profile(current_user: User = Depends(get_current_user)):
    return {"user": current_user.to_dict()}

@router.get("/stats")
async def get_user_stats(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    total_logs = db.query(SpeciesLog).filter(SpeciesLog.user_id == current_user.id).count()
    unique_species = db.query(SpeciesLog.species_id).filter(SpeciesLog.user_id == current_user.id).distinct().count()
    return {"total_logs": total_logs, "unique_species": unique_species}


# maps route 
@router.get("/public/species-locations")
async def get_species_locations(db: Session = Depends(get_db)):
    logs = db.query(SpeciesLog).filter(
        SpeciesLog.location_latitude.isnot(None),
        SpeciesLog.location_longitude.isnot(None)
    ).all()

    response = []

    for log in logs:
        lat = log.location_latitude
        lng = log.location_longitude

        region = get_region_name(lat, lng)  # Reverse geocode once
        response.append({
            "lat": lat,
            "lng": lng,
            "species_id": log.species_id,
            "species_name": log.species.name if log.species else None,
            "region": region
        })

    return response

@router.get("/public/species-images")
async def get_species_images(db: Session = Depends(get_db)):
    species_logs = db.query(SpeciesLog).filter(SpeciesLog.photo_path.isnot(None)).all()

    species_images = {}
    for log in species_logs:
        if log.species_id not in species_images:
            species_images[log.species_id] = {
                "species_id": log.species_id,
                "species_name": log.species.name if log.species else "Unknown",
                "photo_path": log.photo_path
            }

    return list(species_images.values())

