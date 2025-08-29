from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# 假设 app 已在 app.py 中创建
from app import app

db = SQLAlchemy(app)

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    cuisine = db.Column(db.String(64))
    dietary_tags = db.Column(db.String(128))

class UserSession(db.Model):
    __tablename__ = 'user_sessions'
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128), nullable=False)
    preferences = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
