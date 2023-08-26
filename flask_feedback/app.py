from flask import Flask, render_template, jsonify, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, User, Feedback
from forms import RegistrationForm,loginForm, FeedbackForm
from sqlalchemy.exc import IntegrityError
app = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///Test_feedback"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route("/")
def show_homepage():
    feedback = Feedback.query.all()
    if "user_id" in session :
        user=User.query.get(session["user_id"])
        return render_template("homepage.html", posts=feedback, user=user)
    return render_template("homepage.html", posts=feedback)
    


@app.route("/register", methods=["GET","POST"])
def handle_registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username= form.username.data
        email = form.email.data
        password = form.password.data
        user= User.register(first_name,last_name,email,username,password)
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            form.username.errors.append("Username taken, Please try again")
            return render_template("registration.html", form=form)

        session["user_id"] = user.id
        flash ("Account created successfully", "success")
        return redirect("/users/<username>")

    return render_template("registration.html", form=form)

@app.route("/login", methods=["GET","POST"])
def handle_login():
    form = loginForm()
    if form.validate_on_submit():
        username= form.username.data
        password = form.password.data
        user=User.authenticate(username,password)
        if user:
            session["user_id"] = user.id
            return redirect("/")
        else:
            form.username.errors=["invalid username/password"]
           

    return render_template("login.html", form=form)

@app.route("/users/<username>")
def show_user_details(username):
    if "user_id" in session:
        user= User.query.filter_by(username=username).first()
        feedback = Feedback.query.filter_by(username=username).all()
        return render_template("user_details.html", user=user, posts=feedback)
    else:
        return redirect("/login")


@app.route("/logout")
def logout_user():
    session.pop("user_id")
    flash("logged out successfully", "success")
    return redirect ("/login")

@app.route("/users/<username>/feedback/add", methods=["GET","POST"])
def add_feedback(username):
    form = FeedbackForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        feedback= Feedback(title=title, content=content, username=username)
        db.session.add(feedback)
        db.session.commit()
        flash("Thanks for providing Feedback", "success")
        return redirect("/users/<username>" )
        
    return render_template("feedback_form.html", form=form, username=username)
  


@app.route("/feedback/<feedback_id>/update")
def update_feedback(feedback_id):
    post = Feedback.query.get(feedback_id)
    form = FeedbackForm(obj=post)
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        feedback= Feedback(title=title, content=content)
        db.session.add(feedback)
        db.session.commit()
        username = feedback.user.username
        flash("feedback updated", "success")
        return redirect(f"/users/{username}")
    else:
        return render_template("feedback_form.html",form=form)


@app.route("/feedback/<feedback_id>/delete", methods=["POST"])
def delete_feedback(feedback_id):
    feedback = Feedback.query.get(feedback_id)
    username = feedback.user.username
    db.session.delete(feedback)
    db.session.commit()
    flash("Feedback deleted successfully", "success")
    return redirect(f"/users/{username}")



@app.route("/secret")
def show_secret():
    if "user_id" not in session:
        flash ("login to view this page", "danger")
        return redirect("/login")
    return render_template("secret.html")