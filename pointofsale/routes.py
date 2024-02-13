from flask import render_template
from pointofsale import app, db


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/subcategories")
def subcategories():
    return render_template("subcategories.html")


@app.route("/items")
def items():
    return render_template("items.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/startscreen")
def startscreen():
    return render_template("startscreen.html")
