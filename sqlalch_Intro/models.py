"""Models for Blogly."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    def __repr__(self):
        u = self
        return f'<User{u.id}{u.first_name}{u.last_name}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(15), nullable=False)
    last_name = db.Column(db.String(15), nullable=False)
    image_url = db.Column(db.String)


class Post(db.Model):
    __tablename__ = "posts"

    def __repr__(self):
        p = self
        return f'<User{p.id}{p.title}{p.content}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='post')
