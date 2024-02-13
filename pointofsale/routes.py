from flask import render_template
from pointofsale import app, db


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")