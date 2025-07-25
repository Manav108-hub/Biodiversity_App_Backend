# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import router
from utils.database import init_db, get_db
from models.schema import User, Species, Question, SpeciesLog, Answer
import uvicorn
import os
import json
from datetime import datetime
from data.part_c_questions import data  # Import all survey questions

app = FastAPI(title="Biodiversity App API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://bio-moni-web.vercel.app",
        "http://localhost:3000"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Include routes
app.include_router(router)

@app.on_event("startup")
async def startup_event():
    init_db()
    seed_database()

def seed_database():
    """Seed the database with initial data"""
    db = next(get_db())
   
    try:
        # Seed questions if not already present
        if db.query(Question).count() == 0:
            for q_data in data:
                # Handle options field properly
                options_value = None
                if q_data.get("options"):
                    if isinstance(q_data["options"], list):
                        options_value = json.dumps(q_data["options"])
                    else:
                        options_value = q_data["options"]
                
                # Handle details field properly  
                details_value = None
                if q_data.get("details"):
                    if isinstance(q_data["details"], dict):
                        details_value = q_data["details"]  # SQLAlchemy JSON column handles dict directly
                    else:
                        details_value = q_data["details"]
                
                # Create question object with proper data types
                db_question = Question(
                    question_text=q_data["question_text"],
                    question_type=q_data["question_type"],
                    options=options_value,
                    is_required=q_data["is_required"],
                    order_index=q_data["order_index"],
                    section=q_data.get("section", "Part C"),
                    depends_on=q_data.get("depends_on"),  # String question text
                    depends_on_value=q_data.get("depends_on_value"),
                    details=details_value  # Dict for JSON column
                )
                db.add(db_question)
       
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")
        import traceback
        traceback.print_exc()

@app.get("/")
async def root():
    return {
        'message': 'Biodiversity App API',
        'version': '1.0.0',
        'endpoints': {
            'authentication': [
                '/register',
                '/login'
            ],
            'species': [
                '/species',
                '/species (POST - admin only)'
            ],
            'questions': [
                '/questions',
                '/questions (POST - admin only)'
            ],
            'species_logs': [
                '/species-logs',
                '/species-logs (POST)',
            ],
            'admin': [
                '/admin/all-logs',
                '/admin/export-csv',
                '/admin/users'
            ],
            'utility': [
                '/profile',
                '/stats'
            ]
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)