from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar_url = db.Column(db.String(255))
    password = db.Column(db.String(128))

    videos = db.relationship('Video', backref='uploader', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
    votes = db.relationship('Vote', backref='user', lazy=True)

class Video(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    upload_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    upload_time = db.Column(db.DateTime, default=datetime.utcnow)

    comments = db.relationship('Comment', backref='video', lazy=True)
    votes = db.relationship('Vote', backref='video', lazy=True)

class Vote(db.Model):
    __tablename__ = 'vote'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    vote_type = db.Column(db.Enum('infringing', 'not_infringing', name='vote_type'), nullable=False)
    vote_time = db.Column(db.DateTime, default=datetime.utcnow)
    # 添加唯一约束，防止同一个用户对同一个视频投多次
    __table_args__ = (db.UniqueConstraint('user_id', 'video_id', name='_user_video_uc'),)

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('comment.id'))
    create_time = db.Column(db.DateTime, default=datetime.utcnow)

    # 支持嵌套回复（楼中楼）
    replies = db.relationship('Comment',
                              backref=db.backref('parent', remote_side=[id]),
                              lazy=True)
