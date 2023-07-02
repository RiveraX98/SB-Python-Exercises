from flask import Flask, render_template, request, redirect, flash, session
from survey import satisfaction_survey
app = Flask(__name__)
app.config['SECRET_KEY'] = "key"


"""responses = session["responses"]"""


@app.route("/satisfaction")
def show_satisfaction_survey_title_page():
    return render_template("title-page.html")


@app.route("/start", methods=["POST"])
def start_survey():

    session["responses"] = []

    return redirect("/questions/0")


@app.route("/questions/<int:num>")
def show_questions(num):
    curr_question = satisfaction_survey.questions[num]
    responses = session["responses"]

    if (responses is None):
        return redirect("/satisfaction")

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/thanks")

    if (len(responses) != num):
        flash(f"Invalid question id: {num}.")
        return redirect(f"/questions/{len(responses)}")

    return render_template("base.html", curr_question=curr_question)


@app.route("/answer", methods=["POST"])
def handle_question():

    answer = request.form['answer']

    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses

    if (len(responses) == len(satisfaction_survey.questions)):
        return redirect("/thanks")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/thanks")
def thank_user():
    return render_template("thanks.html")
