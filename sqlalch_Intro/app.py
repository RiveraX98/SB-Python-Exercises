"""Blogly application."""

from flask import Flask, render_template, session, request, redirect
from models import db, connect_db, User, Post

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///Test_users'
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
    return render_template("new_user_form.html")


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
    posts = Post.query.filter(Post.user_id == user_id)

    return render_template("details.html", user=user, posts=posts)


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
    return redirect(f"/{user_id}")


@app.route('/<int:user_id>/delete_user', methods=["POST"])
def delete_user(user_id):
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect("/")


@app.route("/users/<int:user_id>/posts/new")
def show_post_form(user_id):

    return render_template("post_form.html", user_id=user_id)


@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    user_id = user_id
    post = Post(title=title, content=content, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return redirect(f"/{user_id}")


@app.route("/posts/<int:post_id>")
def show_posts(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_details.html", post=post)


@app.route("/posts/<int:post_id>/edit")
def show_post_edit(post_id):
    post = Post.query.get(post_id)
    return render_template("edit_post.html", post=post)


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def save_post_edit(post_id):
    title = request.form["title"]
    content = request.form["content"]
    post = Post.query.get(post_id)
    post.title = title
    post.content = content
    db.session.add(post)
    db.session.commit()
    return redirect(f"/posts/{post.id}/edit")


@app.route("/posts/<int:post_id>/delete")
def delete_post(post_id):
    post = Post.query.get(post_id)
    user_id = post.user.id
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect(f"/{user_id}")
