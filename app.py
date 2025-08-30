from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# 配置 SQLite 数据库 URI
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, 'database', 'recipe_db.db')
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 数据模型定义
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    steps = db.Column(db.Text, nullable=False)
    cuisine = db.Column(db.String(64))
    dietary_tags = db.Column(db.String(128))

class UserSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(128), nullable=False)
    preferences = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()
    # 强制写入一条测试数据，确保数据库文件生成
    if not Recipe.query.first():
        test_recipe = Recipe(
            name="测试菜谱",
            ingredients="鸡蛋, 西红柿",
            steps="炒鸡蛋, 加西红柿",
            cuisine="家常",
            dietary_tags="高蛋白"
        )
        db.session.add(test_recipe)
        db.session.commit()

# 根路由，返回前端页面
@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

# 生成食谱API（暂时返回固定JSON）
@app.route('/generate', methods=['POST'])
def generate():
    # 这里可以接收前端传来的数据并处理
    return jsonify({
        "name": "健康鸡胸肉沙拉",
        "ingredients": ["鸡胸肉", "莴苣", "番茄", "橄榄油", "黑胡椒"],
        "steps": ["鸡胸肉煮熟切片", "莴苣和番茄洗净切块", "混合所有食材，加入橄榄油和黑胡椒拌匀"],
        "cuisine": "西式",
        "dietary_tags": "高蛋白、低脂肪"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
