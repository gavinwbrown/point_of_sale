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
        menus = Menus(
            menus_name=request.form.get("menus_name"),
            menus_description = request.form.get("menus_description")
        )
        db.session.add(menus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("add_menus.html")


@app.route("/edit_menus/<int:menus_id>", methods=["GET", "POST"])
def edit_menus(menus_id):
    menus = Menus.query.get_or_404(menus_id)
    if request.method == "POST":
        menus=Menus(
            menus_name=request.form.get("menus_name"),
            menus_description=request.form.get("menus_description")
        )
        db.session.add(menus)
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
    menus = list(Menus.query.order_by(Menus.menus_name).all())
    if request.method == "POST":
        submenus = Submenus(
            submenu_name=request.form.get("submenu_name"),
            submenu_description=request.form.get("submenu_description"),
            menus_id=request.form.get("menus_id")
        )
        db.session.add(submenus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("add_sub_menus.html", menus=menus)

@app.route("/edit_submenus/<int:menus_id>", methods=["GET", "POST"])
def edit_submenus(menus_id):
    submenus = Submenus.query.get_or_404(menus_id)
    if request.method == "POST":
        submenus=Menus(
            submenu_name=request.form.get("submenu_name"),
            submenu_description=request.form.get("submenu_description")
        )
        db.session.add(submenus)
        db.session.commit()
        return redirect(url_for("main_menu"))
    return render_template("edit_submenus.html", sub_menus=submenus)


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
