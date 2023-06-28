# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)


@app.route("/add")
def evaluate_add():
    a = int(request.args["a"])
    b = int(request.args["b"])

    answer = add(a, b)

    return str(answer)


@app.route("/sub")
def evaluate_sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = sub(a, b)

    return str(answer)


@app.route("/mult")
def evaluate_mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = mult(a, b)

    return str(answer)


@app.route("/div")
def evaluate_div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = div(a, b)

    return str(answer)


operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args["a"])
    b = int(request.args["b"])
    answer = operators[oper](a, b)

    return str(answer)
