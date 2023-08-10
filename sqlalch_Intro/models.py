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
    created_at = db.Column(db.DateTime(timezone=True),
                           default=func.now(), nullable=False,)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', backref='post')


class Tag(db.Model):
    __tablename__ = "tags"

    @ classmethod
    def add_tag(cls, tag):
        db.session.add(tag)
        db.session.commit()

    def __repr__(self):
        t = self
        return f'<User{t.id}{t.name}'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False, unique=True)

    posts = db.relationship("Post", secondary="post_tags", backref="tags")


class PostTag(db.Model):
    __tablename__ = "post_tags"

    def __repr__(self):
        p = self
        return f'<User{p.post_id}{p.tag_id}'

    post_id = db.Column(db.Integer, db.ForeignKey(
        "posts.id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True)
