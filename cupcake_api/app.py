from flask import Flask, render_template, jsonify, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import connect_db, db, Cupcake
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config['CORS_HEADERS'] = 'Content-Type'

toolbar = DebugToolbarExtension(app)
connect_db(app)
db.create_all()

@app.route("/")
def show_page():
    return render_template("homepage.html")

@app.route("/api/cupcakes", methods=["GET"])
def lists_cupcakes():
    print("hitEndPoint")
    cupcakes = Cupcake.query.all()
    serialized = [cake.serialize() for cake in cupcakes]
    return jsonify(cupcakes = serialized)


@app.route("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    cupcake= Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    print(request)
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating= request.json["rating"]

    image = request.json.get("image","https://tinyurl.com/demo-cupcake")
    new_cupcake= Cupcake(flavor=flavor, size=size,rating=rating,image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    
    return (jsonify(cupcake=new_cupcake.serialize()), 201)

@app.route("/api/cupcakes/<int:cupcake_id>", methods=["PATCH"])
def update_cupcake(cupcake_id):
    cake = Cupcake.query.get_or_404(cupcake_id)
    db.session.query(Cupcake).filter_by(id = cupcake_id).update(requests.json)
    db.session.commit()
    return jsonify(cupcake= cake.serialize())

@app.route("/api/cupcakes/<int:cupcake_id>", methods = ["DELETE"])
def delete_cupcake(cupcake_id):
    cake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cake)
    db.session.commit()
    return jsonify(deleted=cupcake_id)