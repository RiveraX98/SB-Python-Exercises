from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)


class Pet (db.Model):
    """Adoptable pets table."""
    __tablename__ = "pets"

    def __repr__(self):
        return f'<Pet{self.id}{self.name}{self.species}{self.available}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    photo_url = db.Column(db.String)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, nullable=False, default=True)


class addPet (FlaskForm):
    """Create a form to add a pet."""
    name = StringField("Name", validators=[InputRequired()])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Optional photo")
    age = IntegerField("Age")
    notes = TextAreaField("Notes")
