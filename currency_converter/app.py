from flask import Flask, render_template, request, redirect
import convert
'''from flask_debugtoolbar import DebugToolbarExtension'''
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "debug"
app.config['DEBUG_TB_ENABLED'] = app.debug
'''toolbar = DebugToolbarExtension(app)'''


base_URL = "https://api.exchangerate.host"

convert_data = []


@app.route("/")
def get_exchange_info():

    return render_template("base.html")


@app.route("/verify_form", methods=["POST"])
def verify_form_info():
    convert_from = request.form["from"].upper()
    into = request.form["into"].upper()
    amount = request.form["amount"]
    convert_data.append(convert_from)
    convert_data.append(into)
    convert_data.append(amount)

    if convert.check_info(convert_from, into, amount) == "ok":
        return redirect("/convert")
    else:
        msg = convert.check_info(convert_from, into, amount)
        return render_template("base.html", msg=msg)


@app.route("/convert")
def display_results():
    """api request to convert then dispay converted amount"""
    convert_from = convert_data[0]
    into = convert_data[1]
    amount = convert_data[2]

    converted_amount = convert.convert_currency(convert_from, into, amount)

    return render_template("converted.html", convertedAmount=converted_amount, convertFrom=convert_from, amount=amount, convertTo=into)
