import os

from flask import Flask, request, render_template, session, redirect, url_for

from . import character


app = Flask(__name__)

# setting the secret key to some random bytes. Keep this really secret!
app.secret_key = b"my_super_secret_key"

@app.route("/", methods = ["GET", "POST"])
def home():

    if request.method == "POST":

        character_name = request.form["character_name"]
        error = None

        if not character_name:
            error = "Name is required"

        if error is None:
            session.clear()
            session["character_name"] = character_name
            return redirect(url_for("make_character"))

    return render_template("home.html")

@app.route("/character")
def make_character():

    character_name = session.get("character_name")
    character_name = character.Character("{}".format(character_name))

    return render_template("character.html", character=character_name.for_template())
