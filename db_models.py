from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configure path to instance/database.db
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    return app

# 🔸 Define your models below this line

class UserInfo(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_mail = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    availability = db.Column(db.String(100))
    skills_have = db.Column(db.String(255))
    skills_want = db.Column(db.String(255))

class SkillTable(db.Model):
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100), unique=True, nullable=False)

class SkillRequest(db.Model):
    swap_id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'), nullable=False)
    to_user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'), nullable=False)
    offered_skill_id = db.Column(db.Integer, db.ForeignKey('skill_table.skill_id'), nullable=False)
    requested_skill_id = db.Column(db.Integer, db.ForeignKey('skill_table.skill_id'), nullable=False)
    status = db.Column(db.String(20), default="pending")
    request_time = db.Column(db.DateTime, default=datetime.utcnow)

class Feedback(db.Model):
    feedback_id = db.Column(db.Integer, primary_key=True)
    swap_id = db.Column(db.Integer, db.ForeignKey('skill_request.swap_id'), nullable=False)
    given_by_user_id = db.Column(db.Integer, db.ForeignKey('user_info.user_id'), nullable=False)
    rating = db.Column(db.Integer)
    comment = db.Column(db.Text)
