from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet, addPet

app = Flask(__name__)
app.debug=True
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()


@app.route("/")
def show_listing():
    """List all pets"""
    pets = Pet.query.filter_by(available=True)
    return render_template("hompage.html", pets=pets)


@app.route("/add_pet", methods=["POST", "GET"])
def add_pet():
    """Add a pet to list"""
    form = addPet()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species,
                  photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet.html", form=form)


@app.route("/<int:pet_id>", methods=["POST", "GET"])
def show_details_and_edit(pet_id):
    """Show a pets details and save edits"""
    pet = Pet.query.get(pet_id)
    form = addPet(obj=pet)
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet_details.html", pet=pet, form=form)
