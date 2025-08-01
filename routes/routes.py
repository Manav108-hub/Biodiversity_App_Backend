import os
from typing import List, Optional
from dotenv import load_dotenv
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
from fastapi import Header

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
    x_admin_secret: str = Header(default=None),
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
    current_user: User = Depends(get_current_user)
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
    section: Optional[str] = None
    is_required: bool = True
    order_index: int = 0
    depends_on: Optional[str] = None  # 🔧 NEW: Now accepts question text instead of ID
    depends_on_value: Optional[str] = None  # 🔧 NEW: The value that triggers dependency
    details: Optional[dict] = None  # 🔧 NEW: For storing additional question metadata


@router.get("/questions")
async def get_questions(db: Session = Depends(get_db)):
    return {"questions": [q.to_dict() for q in db.query(Question).order_by(Question.order_index)]}

@router.post("/questions")
async def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    # 🔧 Handle options serialization
    options_json = None
    if question.options:
        options_json = json.dumps(question.options)
    
    db_question = Question(
        question_text=question.question_text,
        question_type=question.question_type,
        options=options_json,  # Store as JSON string
        section=question.section,
        is_required=question.is_required,
        order_index=question.order_index,
        depends_on=question.depends_on,  # Now stores question text
        depends_on_value=question.depends_on_value,
        details=question.details  # SQLAlchemy JSON column handles dict directly
    )
    
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    
    return {
        "message": "Question created successfully",
        "question": db_question.to_dict()
    }

# Add this to your existing routes.py file

class QuestionUpdate(BaseModel):
    question_text: Optional[str] = None
    question_type: Optional[str] = None
    options: Optional[list] = None
    section: Optional[str] = None
    is_required: Optional[bool] = None
    order_index: Optional[int] = None
    depends_on: Optional[str] = None  # Question text reference
    depends_on_value: Optional[str] = None
    details: Optional[dict] = None

@router.put("/questions/{question_id}")
async def update_question(
    question_id: int,
    question_update: QuestionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """
    Update a question by ID. Requires admin access.
    Only provided fields will be updated (partial update).
    """
    # Find the question
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Update only the fields that were provided
    update_data = question_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        if field == "options" and value is not None:
            # Handle options serialization
            setattr(db_question, field, json.dumps(value))
        else:
            setattr(db_question, field, value)
    
    # Commit the changes
    try:
        db.commit()
        db.refresh(db_question)
        return {
            "message": "Question updated successfully",
            "question": db_question.to_dict()
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to update question: {str(e)}")

# Optional: Bulk update endpoint for updating multiple questions at once
class BulkQuestionUpdate(BaseModel):
    questions: List[dict]  # List of {"id": int, "updates": QuestionUpdate}

@router.put("/questions/bulk")
async def bulk_update_questions(
    bulk_update: BulkQuestionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """
    Update multiple questions at once. Requires admin access.
    Format: {"questions": [{"id": 1, "updates": {...}}, {"id": 2, "updates": {...}}]}
    """
    updated_questions = []
    errors = []
    
    for item in bulk_update.questions:
        question_id = item.get("id")
        updates = item.get("updates", {})
        
        try:
            # Find the question
            db_question = db.query(Question).filter(Question.id == question_id).first()
            if not db_question:
                errors.append(f"Question with ID {question_id} not found")
                continue
            
            # Apply updates
            for field, value in updates.items():
                if field == "options" and value is not None:
                    setattr(db_question, field, json.dumps(value))
                else:
                    setattr(db_question, field, value)
            
            updated_questions.append(db_question.to_dict())
            
        except Exception as e:
            errors.append(f"Failed to update question {question_id}: {str(e)}")
    
    try:
        db.commit()
        return {
            "message": f"Updated {len(updated_questions)} questions successfully",
            "updated_questions": updated_questions,
            "errors": errors if errors else None
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to commit updates: {str(e)}")

# DELETE endpoints for questions
@router.delete("/questions/{question_id}")
async def delete_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """
    Delete a question by ID. Requires admin access.
    Note: This will also delete all associated answers due to cascade relationships.
    """
    # Find the question
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Check if there are any answers associated with this question
    answer_count = db.query(Answer).filter(Answer.question_id == question_id).count()
    
    try:
        # Store question info for response before deletion
        question_info = db_question.to_dict()
        
        # Delete the question (answers will be deleted automatically due to cascade)
        db.delete(db_question)
        db.commit()
        
        return {
            "message": f"Question deleted successfully. {answer_count} associated answers were also removed.",
            "deleted_question": question_info,
            "affected_answers": answer_count
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to delete question: {str(e)}")

# Bulk delete endpoint
class BulkQuestionDelete(BaseModel):
    question_ids: List[int]

@router.delete("/questions/bulk")
async def bulk_delete_questions(
    bulk_delete: BulkQuestionDelete,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """
    Delete multiple questions at once. Requires admin access.
    Format: {"question_ids": [1, 2, 3, 4]}
    """
    deleted_questions = []
    errors = []
    total_affected_answers = 0
    
    for question_id in bulk_delete.question_ids:
        try:
            # Find the question
            db_question = db.query(Question).filter(Question.id == question_id).first()
            if not db_question:
                errors.append(f"Question with ID {question_id} not found")
                continue
            
            # Count associated answers
            answer_count = db.query(Answer).filter(Answer.question_id == question_id).count()
            total_affected_answers += answer_count
            
            # Store question info before deletion
            question_info = db_question.to_dict()
            question_info['affected_answers'] = answer_count
            
            # Delete the question
            db.delete(db_question)
            deleted_questions.append(question_info)
            
        except Exception as e:
            errors.append(f"Failed to delete question {question_id}: {str(e)}")
    
    try:
        db.commit()
        return {
            "message": f"Deleted {len(deleted_questions)} questions successfully",
            "deleted_questions": deleted_questions,
            "total_affected_answers": total_affected_answers,
            "errors": errors if errors else None
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to commit deletions: {str(e)}")

# Soft delete option (marks as deleted instead of removing from database)
@router.patch("/questions/{question_id}/archive")
async def archive_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):
    """
    Archive/soft delete a question by ID. Requires admin access.
    Note: This requires adding an 'is_active' or 'archived' field to your Question model.
    This is a safer alternative to hard deletion.
    """
    # Find the question
    db_question = db.query(Question).filter(Question.id == question_id).first()
    if not db_question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    # Note: You would need to add an 'is_active' boolean field to your Question model
    # For now, this is a placeholder implementation
    
    # If you add is_active field to Question model, uncomment below:
    # db_question.is_active = False
    # db.commit()
    # db.refresh(db_question)
    
    return {
        "message": "Archive feature requires adding 'is_active' field to Question model",
        "suggestion": "Consider adding 'is_active = Column(Boolean, default=True)' to Question model for soft deletes"
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

@router.get("/questions-with-dependencies")
async def get_questions_with_dependencies(db: Session = Depends(get_db)):
    """Get questions with resolved dependency information"""
    questions = db.query(Question).order_by(Question.order_index).all()
    
    # Create a mapping for easier dependency resolution
    question_map = {q.question_text: q.to_dict() for q in questions}
    
    result = []
    for question in questions:
        q_dict = question.to_dict()
        
        # Add dependency information if it exists
        if question.depends_on and question.depends_on in question_map:
            q_dict['depends_on_question'] = {
                'id': question_map[question.depends_on]['id'],
                'question_text': question.depends_on,
                'value_required': question.depends_on_value
            }
        
        result.append(q_dict)
    
    return {"questions": result}

