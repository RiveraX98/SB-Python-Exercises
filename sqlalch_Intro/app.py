"""Blogly application."""

from flask import Flask, render_template, session, request, redirect
from models import db, connect_db, User

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)


@app.route('/')
def list_users():
    users = User.query.all()
    return render_template('base.html', users=users)


@app.route('/new_user_form')
def new_user_form():
    return render_template("form.html")


@app.route('/create_user', methods=["POST"])
def create_user():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    url = request.form["photo_url"]
    new_user = User(first_name=first_name, last_name=last_name, image_url=url)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/{new_user.id}")


@app.route("/<int:user_id>")
def show_user_details(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("details.html", user=user)


@app.route('/<int:user_id>/edit')
def show_edit_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit.html", user=user)


@app.route('/<int:user_id>', methods=["POST"])
def save_user_changes(user_id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    url = request.form["photo_url"]
    user = User.query.get(user_id)
    user.first_name = first_name
    user.last_name = last_name
    user.image_url = url
    db.session.add(user)
    db.session.commit()
    return redirect(f"/{user.id}")


@app.route('/<int:user_id>/delete_user', methods=["POST"])
def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect("/")
