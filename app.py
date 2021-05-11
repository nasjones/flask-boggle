from boggle import Boggle
from flask import Flask, session, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension

boggle_game = Boggle()
app = Flask(__name__)
app.config["SECRET_KEY"] = "hush"
debug = DebugToolbarExtension(app)


@app.route('/')
def game_run():
    """
    This function initializes the game upon landing 
    on the homepage
    """
    session['board'] = boggle_game.make_board()
    session['guesses'] = []
    return render_template("home.html", board=session['board'])


@app.route('/answer_attempt', methods=["POST"])
def answer_attempt():
    """
    This function allows answer attempts to be posted to 
    the endpoint
    """
    attempt = request.get_json()['attempt']
    return jsonify(result=exists(attempt))


def exists(word):
    """
    This function accepts a string and checks if it has
    already been entered and if it hasn't then checks 
    if the word is valid
    """
    if word in session['guesses']:
        response = "Already guessed"
    else:
        guesses = session['guesses']
        guesses.append(word)
        session['guesses'] = guesses
        response = boggle_game.check_valid_word(session['board'], word)
    return response
