from flask import Flask, session, render_template, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "debug"
app.config['DEBUG_TB_ENABLED'] = app.debug
toolbar = DebugToolbarExtension(app)


boggle_game = Boggle()


@app.route("/")
def homepage():
    """Show board."""

    board = boggle_game.make_board()
    session["board"] = board
    return render_template("base.html", board=board)


@app.route("/check-word")
def check_guessed_word():
    word = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, word)
    return jsonify({'result': response})


"""def generateKey(length):
    chars = "ABCDEFGHIJKLXYZ1234567890"
    for i in range(length):
        return """
