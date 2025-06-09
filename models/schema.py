from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base
import bcrypt
import json

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    species_logs = relationship("SpeciesLog", backref="user", cascade="all, delete-orphan")
    
    def set_password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat()
        }

class Species(Base):
    __tablename__ = 'species'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    scientific_name = Column(String(100), nullable=True)
    category = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    species_logs = relationship("SpeciesLog", backref="species")
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'scientific_name': self.scientific_name,
            'category': self.category,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

class Question(Base):
    __tablename__ = 'questions'
    
    id = Column(Integer, primary_key=True)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(20), nullable=False)
    options = Column(Text, nullable=True)
    is_required = Column(Boolean, default=True)
    order_index = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def get_options(self):
        return json.loads(self.options) if self.options else []
    
    def set_options(self, options_list: list):
        self.options = json.dumps(options_list)
    
    def to_dict(self):
        return {
            'id': self.id,
            'question_text': self.question_text,
            'question_type': self.question_type,
            'options': self.get_options(),
            'is_required': self.is_required,
            'order_index': self.order_index,
            'created_at': self.created_at.isoformat()
        }

class SpeciesLog(Base):
    __tablename__ = 'species_logs'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'), nullable=False)
    location_latitude = Column(Float, nullable=True)
    location_longitude = Column(Float, nullable=True)
    location_name = Column(String(200), nullable=True)
    photo_path = Column(String(300), nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    answers = relationship("Answer", backref="species_log", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'species_id': self.species_id,
            'species_name': self.species.name if self.species else None,
            'location_latitude': self.location_latitude,
            'location_longitude': self.location_longitude,
            'location_name': self.location_name,
            'photo_path': self.photo_path,
            'notes': self.notes,
            'created_at': self.created_at.isoformat(),
            'answers': [answer.to_dict() for answer in self.answers]
        }

class Answer(Base):
    __tablename__ = 'answers'
    
    id = Column(Integer, primary_key=True)
    species_log_id = Column(Integer, ForeignKey('species_logs.id'), nullable=False)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False)
    answer_text = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    question = relationship("Question", backref="answers")
    
    def to_dict(self):
        return {
            'id': self.id,
            'species_log_id': self.species_log_id,
            'question_id': self.question_id,
            'question_text': self.question.question_text if self.question else None,
            'answer_text': self.answer_text,
            'created_at': self.created_at.isoformat()
        }