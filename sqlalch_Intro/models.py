"""Models for Blogly."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()



def connect_db(app):
    db.app=app
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



