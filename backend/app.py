from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import datetime

app = Flask(__name__)

# 配置 SQLite 数据库 URI
base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(base_dir, '..', 'database')
os.makedirs(db_dir, exist_ok=True)  # 确保 database 目录存在

db_path = os.path.join(db_dir, 'recipe_db.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'AI个性化食谱生成器后端已启动！'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)