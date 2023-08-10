"""Blogly application."""

from flask import Flask, render_template, session, request, redirect, flash
from models import db, connect_db, User, Post, Tag, PostTag
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'


toolbar = DebugToolbarExtension(app)
connect_db(app)


@app.route("/")
def show_hompage():
    posts = Post.query.order_by("created_at").limit(3).all()
    return render_template("homepage.html", posts=posts)


@app.route('/users')
def list_users():
    users = User.query.all()
    return render_template('all_users.html', users=users)


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

    return render_template("user_details.html", user=user, posts=posts)


@app.route('/<int:user_id>/edit')
def show_edit_form(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("edit_user.html", user=user)


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
    return redirect("/users")


@app.route("/users/<int:user_id>/posts/new")
def show_post_form(user_id):
    tags = Tag.query.all()
    return render_template("post_form.html", user_id=user_id, tags=tags)


@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post(user_id):
    title = request.form["title"]
    content = request.form["content"]
    new_post = Post(
        title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    post = Post.query.filter(
        Post.title == title, Post.user_id == user_id).one()

    checked_tags = [int(num) for num in request.form.getlist("tags")]

    tags = Tag.query.filter(Tag.id.in_(checked_tags)).all()
    for tag in checked_tags:
        new_postTag = PostTag(post_id=post.id, tag_id=tag)
        db.session.add(new_postTag)
        db.session.commit()

    return redirect(f"/{user_id}")


@app.route("/posts")
def show_posts():
    posts = Post.query.all()
    return render_template("all_posts.html", posts=posts)


@app.route("/posts/<int:post_id>")
def show_posts_details(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post_details.html", post=post)


@app.route("/posts/<int:post_id>/edit")
def show_post_edit(post_id):
    post = Post.query.get(post_id)
    return render_template("edit_post.html", post=post)


@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def edit_post(post_id):
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
    PostTag.query.filter_by(post_id=post_id).delete()
    Post.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect(f"/{user_id}")


@app.route("/tags")
def show_tags():
    tags = Tag.query.all()
    return render_template("all_tags.html", tags=tags)


@app.route("/tags/new")
def show_tag_form():
    return render_template("tag_form.html")


@app.route("/tags/new", methods=["POST"])
def add_new_tag():
    new_tag = request.form["tag"]
    tag = Tag(name=new_tag)
    tag.add_tag(tag)

    return redirect("/tags")


@app.route("/tag/<int:tag_id>")
def show_tag_posts(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template("tag_posts.html", tag=tag)


@app.route("/tag/<int:tag_id>/delete")
def delete_tag(tag_id):
    Tag.query.filter_by(id=tag_id).delete()
    db.session.commit()
    return redirect("/tags")


@app.route("/tag/<int:tag_id>/edit")
def show_tag_edit(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template("edit_tag.html", tag=tag)


@app.route("/tag/<int:tag_id>/edit", methods=["POST"])
def edit_tag(tag_id):
    name = request.form["tag"]
    tag = Tag.query.get(tag_id)
    tag.name = name
    tag.add_tag(tag)
    return redirect(f"/tag/{tag_id}")
