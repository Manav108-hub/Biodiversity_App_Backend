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
from data.part_c_questions import part_c_questions  # Import Part C questions

app = FastAPI(title="Biodiversity App API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
        # Create admin user if not exists (optional)
        if db.query(User).count() == 0:
            admin_user = User(
                username='admin',
                email='admin@example.com',
                is_admin=True
            )
            admin_user.set_password('admin123')
            db.add(admin_user)
        
        # Seed only Part C questions
        if db.query(Question).count() == 0:
            for q_data in part_c_questions:
                db_question = Question(**q_data)
                if q_data.get("options"):
                    db_question.set_options(json.loads(q_data["options"]))
                db.add(db_question)
        
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error seeding database: {e}")

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