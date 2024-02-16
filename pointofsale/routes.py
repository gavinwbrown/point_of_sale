from flask import render_template, request, redirect, url_for
from pointofsale import app, db
from pointofsale.models import Menus, Submenus, Items


@app.route("/")
def home():
    return render_template("startscreen.html")


@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html")


@app.route("/add_menu", methods=["GET", "POST"])
def add_menu():
    return render_template("add_menu.html")


@app.route("/add_sub_menu", methods=["GET", "POST"])
def add_sub_menu():
    return render_template("add_sub_menu.html")


@app.route("/add_item", methods=["GET", "POST"])
def add_item():
    return render_template("add_item.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/startscreen")
def startscreen():
    return render_template("startscreen.html")
