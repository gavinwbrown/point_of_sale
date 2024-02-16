from flask import render_template, request, redirect, url_for
from pointofsale import app, db
from pointofsale.models import Menus, Submenus, Items


@app.route("/")
def home():
    return render_template("startscreen.html")


@app.route("/main_menu")
def main_menu():
    menus = list(Menus.query.order_by(Menus.menus_name).all())
    return render_template("main_menu.html", menus=menus)


@app.route("/add_menus", methods=["GET", "POST"])
def add_menus():
    if request.method == "POST":
        menus = Menus(menus_name=request.form.get("menus_name"))
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("add_menus.html")


@app.route("/edit_menus/<int:menus_id>", methods=["GET", "POST"])
def edit_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        menus.menus_name = request.form.get("menus_name")
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("edit_menus.html", menus=menus)

@app.route("/delete_menus/<int:menus_id>")
def delete_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    db.session.delete(menus)
    db.session.commit()
    return redirect(url_for("main_menu"))


@app.route("/add_sub_menus", methods=["GET", "POST"])
def add_sub_menus():
    return render_template("add_sub_menus.html")


@app.route("/add_items", methods=["GET", "POST"])
def add_items():
    return render_template("add_items.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/startscreen")
def startscreen():
    return render_template("startscreen.html")
